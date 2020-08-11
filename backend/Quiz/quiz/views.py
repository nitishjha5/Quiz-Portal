from django.shortcuts import render
from myapi.serializers import QuizSerializer,QuestionsSerializer,OptionSerializer,AttemptSerializer,PerfomanceSerializer
from rest_framework import viewsets
from quiz.models import Quiz,Questions,Option
from account.models import Attempt,Perfomance
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions 

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]  # added

    def get_queryset(self):  # added
        return self.request.user.quizs.all()

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

# Create your views here.
