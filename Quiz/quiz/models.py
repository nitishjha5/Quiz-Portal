from django.db import models
import datetime



class Quiz(models.Model):

	title=models.CharField(max_length=100)
    #starttime=models.DateTimeField(auto_now=False,auto_now_add=False) 
    #endtime=models.DateTimeField(auto_now=False,auto_now_add=False )
	no_of_ques=models.IntegerField()
	full_marks=models.DecimalField(max_digits=5, decimal_places=2)
	user=models.ForeignKey('account.Student',on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Questions(models.Model):
	quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
	text=models.TextField()
	image=models.ImageField(blank=True)
	mark=models.DecimalField(max_digits=5, decimal_places=2)

class Option(models.Model):
	ques=models.ForeignKey(Questions,on_delete=models.CASCADE)
	text=models.TextField()
	image=models.ImageField(blank=True)
	iscoorect= models.BooleanField()


	
	
	

# Create your models here.



# Create your models here.
