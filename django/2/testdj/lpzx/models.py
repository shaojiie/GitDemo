from django.db import models

# Create your models here.
class user(models.Model):
	comname	= models.CharField(max_length=20)
	groupname	= models.CharField(max_length=20)
	usercode	= models.CharField(max_length=10)
	username	= models.CharField(max_length=20)
	post	= models.CharField(max_length=10)
	postcode  = models.CharField(max_length=3)