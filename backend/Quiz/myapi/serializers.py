from rest_framework import serializers
from django.contrib.auth import authenticate
from quiz.models import Quiz,Questions,Option
from account.models import Attempt,Perfomance
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token







class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = ( 'id','select','text','image')
class QuestionsSerializer(serializers.HyperlinkedModelSerializer):
    options=OptionSerializer(many=True)
    
    class Meta:
        model = Questions
        fields = ('qno','text','image','options','mark')

class QuizSerializer(serializers.ModelSerializer):
    question=QuestionsSerializer(many=True)
    class Meta:
        model = Quiz
        fields = ('student','question','title', 'start_time','end_time','no_of_ques','full_marks')








class AttemptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attempt
        fields = ('user', 'quiz','question','option')

class PerfomanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfomance
        fields = ('marks_obtained', 'rank','user','quiz')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")