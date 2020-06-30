from rest_framework import serializers

from quiz.models import Quiz,Questions,Option
from account.models import Batch,Student,Attempt,Perfomance
from django.contrib.auth.models import User



class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'start_time','end_time','no_of_ques','full_marks','batch')

class QuestionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questions
        fields = ('quiz', 'qno','text','image','mark')

class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = ('question', 'text','image','iscorrect')

class BatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Batch
        fields = ('batch')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('user', 'name','email','batch')

 
class AttemptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attempt
        fields = ('user', 'quiz','question','option')

class PerfomanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfomance
        fields = ('marks_obtained', 'rank','user','quiz')
 
 