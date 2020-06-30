from django.shortcuts import render
from rest_framework import viewsets

from .serializers import QuizSerializer,QuestionsSerializer,OptionSerializer,BatchSerializer,StudentSerializer,AttemptSerializer,PerfomanceSerializer
from quiz.models import Quiz,Questions,Option
from account.models import Batch,Student,Attempt,Perfomance
from django.contrib.auth.models import User


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class AttemptViewSet(viewsets.ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer

class PerfomanceViewSet(viewsets.ModelViewSet):
    queryset = Perfomance.objects.all()
    serializer_class = PerfomanceSerializer

# Create your views here.
