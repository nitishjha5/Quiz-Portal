from rest_framework import serializers
from django.contrib.auth import authenticate
from quiz.models import Quiz,Question,Option,QuizTaker,UsersAnswer

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class QuizListSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    class Meta:
        model = Quiz
        fields = ["id", "title", "slug", "questions_count"]
        read_only_fields = ["questions_count"]

    def get_questions_count(self, obj):
        return obj.question_set.all().count()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["id", "question", "text","image"]


class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"


class UsersAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersAnswer
        fields = "__all__"

class MyQuizListSerializer(serializers.ModelSerializer):
    completed = serializers.SerializerMethodField()
    questions_count = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ["id", "title", "slug", "questions_count", "completed", "score"]
        read_only_fields = ["questions_count", "completed"]

    def get_completed(self, obj):
        try:
            quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
            return quiztaker.completed
        except QuizTaker.DoesNotExist:
            return None

   
    def get_questions_count(self, obj):
        return obj.question_set.all().count()
    def get_score(self, obj):
        try:
            quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
            if quiztaker.completed == True:
                return quiztaker.score
            return None
        except QuizTaker.DoesNotExist:
            return None


class QuizTakerSerializer(serializers.ModelSerializer):
    usersanswer_set = UsersAnswerSerializer(many=True)

    class Meta:
        model = QuizTaker
        fields = "__all__"

class QuizDetailSerializer(serializers.ModelSerializer):
    quiztakers_set = serializers.SerializerMethodField()
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = "__all__"

    def get_quiztakers_set(self, obj):
        try:
            quiz_taker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
            serializer = QuizTakerSerializer(quiz_taker)
            return serializer.data
        except QuizTaker.DoesNotExist:
            return None


class QuizResultSerializer(serializers.ModelSerializer):
    quiztaker_set = serializers.SerializerMethodField()
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Quiz  
        fields = "__all__"

    def get_quiztaker_set(self, obj):
        try:
            quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
            serializer = QuizTakerSerializer(quiztaker)
            return serializer.data

        except QuizTaker.DoesNotExist:
            return None 


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
        if user :
            return user
        raise serializers.ValidationError("Incorrect Credentials")