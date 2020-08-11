from django.db import models
from django.contrib.auth.models import User
	 
	


class Attempt(models.Model):
	
	quiz=models.ForeignKey('quiz.Quiz',on_delete=models.CASCADE)
	question=models.ForeignKey('quiz.Questions',on_delete=models.CASCADE)
	option=models.ForeignKey('quiz.Option',on_delete=models.CASCADE)

class Perfomance(models.Model):
	
	marks_obtained=models.DecimalField(max_digits=5, decimal_places=2)
	rank=models.IntegerField()
	
	quiz=models.ForeignKey('quiz.Quiz',on_delete=models.CASCADE)
	# Create your models here.
