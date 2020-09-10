
from django.contrib import admin
import nested_admin
from .models import Quiz,Question,Option,UsersAnswer,QuizTaker


class AnswerInline(nested_admin.NestedTabularInline):
	model = Option
	
	max_num = 4


class QuestionInline(nested_admin.NestedTabularInline):
	model = Question
	inlines = [AnswerInline,]
	


class QuizAdmin(nested_admin.NestedModelAdmin):
	inlines = [QuestionInline,]


class UsersAnswerInline(admin.TabularInline):
	model = UsersAnswer


class QuizTakerAdmin(admin.ModelAdmin):
	inlines = [UsersAnswerInline,]

admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(QuizTaker,QuizTakerAdmin)
admin.site.register(UsersAnswer)


