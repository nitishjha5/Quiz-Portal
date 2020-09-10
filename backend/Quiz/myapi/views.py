from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import MyQuizListSerializer, QuizDetailSerializer, QuizListSerializer, QuizResultSerializer, UsersAnswerSerializer, QuestionSerializer,AnswerSerializer,UserSerializer, RegisterSerializer, LoginSerializer,QuizDetailSerializer
from quiz.models import Quiz,Question,Option,QuizTaker,UsersAnswer

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions  # added permissions
from rest_framework import generics,status
from rest_framework.response import Response
from knox.models import AuthToken

class MyQuizListAPI(generics.ListAPIView):
    
    serializer_class = MyQuizListSerializer
    

    def get_queryset(self, *args, **kwargs):
        queryset = Quiz.objects.filter(quiztaker__user=self.request.user)
        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
            ).distinct()

        return queryset


class QuizListAPI(generics.ListAPIView):
    serializer_class = QuizListSerializer
    
    
    def get_queryset(self, *args, **kwargs):
        queryset = Quiz.objects.filter(roll_out=True)
        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
            ).distinct()

        return queryset


class QuizDetailAPI(generics.RetrieveAPIView):
    serializer_class = QuizDetailSerializer
    
    

    def get(self, *args, **kwargs):
        slug = self.kwargs["slug"]
        quiz = get_object_or_404(Quiz, slug=slug)
        last_question = None
        obj, created = QuizTaker.objects.get_or_create(user=self.request.user, quiz=quiz)
        if created:
            for question in Question.objects.filter(quiz=quiz):
                UsersAnswer.objects.create(quiz_taker=obj, question=question)
        else:
            last_question = UsersAnswer.objects.filter(quiz_taker=obj, answer__isnull=False)
            if last_question.count() > 0:
                last_question = last_question.last().question.id
            else:
                last_question = None

        return Response({'quiz': self.get_serializer(quiz, context={'request': self.request}).data, 'last_question_id': last_question})


class SaveUsersAnswer(generics.UpdateAPIView):
    serializer_class = UsersAnswerSerializer
    

    def patch(self, request, *args, **kwargs):
        quiztaker_id = request.data['quiztaker']
        question_id = request.data['question']
        answer_id = request.data['answer']

        quiztaker = get_object_or_404(QuizTaker, id=quiztaker_id)
        question = get_object_or_404(Question, id=question_id)
        answer = get_object_or_404(Option, id=answer_id)

        if quiztaker.completed:
            return Response({
                "message": "This quiz is already complete. you can't answer any more questions"},
                status=status.HTTP_412_PRECONDITION_FAILED
            )

        obj = get_object_or_404(UsersAnswer, quiz_taker=quiztaker, question=question)
        obj.answer = answer
        obj.save()

        return Response(self.get_serializer(obj).data)


class SubmitQuizAPI(generics.GenericAPIView):
    serializer_class = QuizResultSerializer
    

    def post(self, request, *args, **kwargs):
        quiztaker_id = request.data['quiztaker']
        question_id = request.data['question']
        answer_id = request.data['answer']

        quiztaker = get_object_or_404(QuizTaker, id=quiztaker_id)
        question = get_object_or_404(Question, id=question_id)

        quiz = Quiz.objects.get(slug=self.kwargs['slug'])

        if quiztaker.completed:
            return Response({
                "message": "This quiz is already complete. You can't submit again"},
                status=status.HTTP_412_PRECONDITION_FAILED
            )

        if answer_id is not None:
            answer = get_object_or_404(Option, id=answer_id)
            obj = get_object_or_404(UsersAnswer, quiz_taker=quiztaker, question=question)
            obj.answer = answer
            obj.save()

        quiztaker.completed = True
        correct_answers = 0

        for users_answer in UsersAnswer.objects.filter(quiz_taker=quiztaker):
            answer = Answer.objects.get(question=users_answer.question, is_correct=True)
            print(answer)
            print(users_answer.answer)
            if users_answer.answer == answer:
                correct_answers += 1

        quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)
        print(quiztaker.score)
        quiztaker.save()

        return Response(self.get_serializer(quiz).data)



class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user





class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "token": AuthToken.objects.create(user)[1]
        })





class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Create your views here.
