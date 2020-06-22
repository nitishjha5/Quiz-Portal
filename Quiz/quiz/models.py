from django.db import models
from datetime import datetime 
from django.utils import timezone   


class Quiz(models.Model):
	title=models.CharField(max_length=100)
	start_time=models.DateTimeField(default=timezone.now)
	end_time=models.DateTimeField(default=timezone.now)
	no_of_ques=models.IntegerField()
	full_marks=models.DecimalField(max_digits=5, decimal_places=2)
	batch=models.ForeignKey('account.Batch',on_delete=models.CASCADE)
	def __str__(self):
		return self.title

class Questions(models.Model):
	quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
	qno=models.IntegerField(unique=True)
	text=models.TextField()
	image=models.ImageField(blank=True)
	mark=models.DecimalField(max_digits=5, decimal_places=2)
	def __str__(self):
		return self.text[:10]

class Option(models.Model):
	ques=models.ForeignKey(Questions,on_delete=models.CASCADE)
	text=models.TextField()
	image=models.ImageField(blank=True)
	iscoorect= models.BooleanField()


	
	
	

# Create your models here.



# Create your models here.
