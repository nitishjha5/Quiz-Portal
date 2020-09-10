from django.conf import settings
from django.db import models
from datetime import datetime 
from django.utils import timezone   
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Quiz(models.Model):
	title=models.CharField(max_length=100)
	slug = models.SlugField(blank=True)
	roll_out = models.BooleanField(default=False)
	time_stamp=models.DateTimeField(default=timezone.now)
	class Meta:
		ordering = ['time_stamp',]
		verbose_name_plural = "Quizzes"

	def __str__(self):
		return self.title

class Question(models.Model):
	quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
	text=models.TextField()
	image=models.ImageField(blank=True)
	mark=models.IntegerField(default=0)
	def __str__(self):
		return self.text

class Option(models.Model):
	question=models.ForeignKey(Question,related_name='answer_set',on_delete=models.CASCADE)
	text=models.TextField(max_length=100)
	image=models.ImageField(blank=True)
	iscorrect= models.BooleanField(default=False)
	def __str__(self):
		return self.text
	#select=models.BooleanField(default=False)

class QuizTaker(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	completed = models.BooleanField(default=False)
	date_finished = models.DateTimeField(null=True)
	timestamp = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.user.username


class UsersAnswer(models.Model):
	quiz_taker = models.ForeignKey(QuizTaker,related_name='usersanswer_set', on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.ForeignKey(Option, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.question.text

@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.title)
	
	
	

# Create your models here.



# Create your models here.
