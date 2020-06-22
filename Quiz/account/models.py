from django.db import models
from django.contrib.auth.models import User

class Batch(models.Model):
	batch=models.CharField(max_length=100)
	def __str__(self):
		return self.batch

class Student(models.Model):
	 user = models.OneToOneField(User, on_delete=models.CASCADE)
	 name=models.CharField(max_length=100)
	 email=models.EmailField(max_length=254)
	 batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
	 
	


class Attempt(models.Model):
	user=models.ForeignKey(Student,on_delete=models.CASCADE)
	quiz=models.ForeignKey('quiz.Quiz',on_delete=models.CASCADE)
	question=models.ForeignKey('quiz.Questions',on_delete=models.CASCADE)
	optioon=models.ForeignKey('quiz.Option',on_delete=models.CASCADE)

class Perfomance(models.Model):
	user=models.ForeignKey(Student,on_delete=models.CASCADE)
	quiz=models.ForeignKey('quiz.Quiz',on_delete=models.CASCADE)
	marks_obtained=models.DecimalField(max_digits=5, decimal_places=2)
	rank=models.IntegerField()
	# Create your models here.
