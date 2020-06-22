from django.db import models
class Batch(models.Model):
	batch=models.CharField(max_length=100)

class Student(models.Model):

	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=254)
	password = models.CharField(max_length=50)
	batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
	
	# Create your models here.
