from rest_framework import serializers

from quiz.models import Quiz,Questions,Option
from account.models import Batch,Student,Attempt,Perfomance
from django.contrib.auth.models import User



class QuizSerializer(serializers.ModelSerializer):
    question=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ('question','title', 'start_time','end_time','no_of_ques','full_marks','batch')

class QuestionsSerializer(serializers.HyperlinkedModelSerializer):
    options=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Questions
        fields = ('qno','text','image','options','mark')

class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = ( 'text','image','iscorrect')

class BatchSerializer(serializers.HyperlinkedModelSerializer):
    student=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Batch
        fields = ('batch','student')



class StudentSerializer(serializers.HyperlinkedModelSerializer):
    #students=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ( 'email','name')

 
class AttemptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attempt
        fields = ('user', 'quiz','question','option')

class PerfomanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfomance
        fields = ('marks_obtained', 'rank','user','quiz')
 
 