from django.shortcuts import render
from rest_framework import viewsets
from .serializers import QuizSerializer,QuestionsSerializer,OptionSerializer,AttemptSerializer,PerfomanceSerializer,UserSerializer, RegisterSerializer, LoginSerializer
from quiz.models import Quiz,Questions,Option
from account.models import Attempt,Perfomance
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions  # added permissions
from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    

    

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class AttemptViewSet(viewsets.ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer

class PerfomanceViewSet(viewsets.ModelViewSet):
    queryset = Perfomance.objects.all()
    serializer_class = PerfomanceSerializer

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
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })





class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Create your views here.
