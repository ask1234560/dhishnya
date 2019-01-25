from django.db import models

# Create your models here.

class dhishnyadb(models.Model):
	name=models.CharField(max_length=200, blank=True)
	email=models.CharField(max_length=200, blank=True, unique=True)
	college=models.CharField(max_length=200, blank=True)
	phone=models.CharField(max_length=200, blank=True)
	date_creating=models.DateTimeField(auto_now=True)
