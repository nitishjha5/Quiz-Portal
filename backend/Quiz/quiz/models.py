from django.db import models
from datetime import datetime 
from django.utils import timezone   
from django.contrib.auth.models import User


class Quiz(models.Model):
	title=models.CharField(max_length=100)
	start_time=models.DateTimeField(default=timezone.now)
	end_time=models.DateTimeField(default=timezone.now)
	no_of_ques=models.IntegerField()
	full_marks=models.DecimalField(max_digits=5, decimal_places=2)
	
	def __str__(self):
		return self.title

class Questions(models.Model):
	quiz=models.ForeignKey(Quiz,related_name='question',on_delete=models.CASCADE)
	qno=models.IntegerField(unique=True)
	text=models.TextField()
	image=models.ImageField(blank=True)
	mark=models.DecimalField(max_digits=5, decimal_places=2)
	def __str__(self):
		return self.text[:10]

class Option(models.Model):
	questions=models.ForeignKey(Questions,related_name='options',on_delete=models.CASCADE)
	text=models.TextField()
	image=models.ImageField(blank=True)
	iscorrect= models.BooleanField()


	
	
	

# Create your models here.



# Create your models here.
