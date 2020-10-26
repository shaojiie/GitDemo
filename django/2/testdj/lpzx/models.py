from django.db import models
from django.urls import reverse

# Create your models here.
class user(models.Model):
	comname	= models.CharField(max_length=20)
	groupname	= models.CharField(max_length=20)
	usercode	= models.CharField(max_length=10)
	username	= models.CharField(max_length=20)
	post	= models.CharField(max_length=10)
	postcode  = models.CharField(max_length=3)

	def get_absolute_url(self):
		# return f"/product/{self.id}"
		return reverse("lpzx:lpzx-detail",kwargs={"id": self.id})

	def del_absolute_url(self):
		# return f"/product/{self.id}/delete/"
		return reverse("lpzx:lpzx-delete",kwargs={"id": self.id})

	def update_absolute_url(self):
		# return f"/product/{self.id}/delete/"
		return reverse("lpzx:lpzx-update",kwargs={"id": self.id})

	# def del_absolute_url(self):
	# 	# return f"/product/{self.id}/delete/"
	# 	return reverse("lpzx:lpzx-delete",kwargs={"id": self.id})