from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class Customuser(AbstractUser):
	clg=models.CharField(max_length=255)
	mob=models.CharField(max_length=255)