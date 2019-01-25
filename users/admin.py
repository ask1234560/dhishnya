from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .forms import Customusercreationform,Customuserchangeform
from .models import Customuser

class Customuseradmin(UserAdmin):
	add_form=Customusercreationform
	form=Customuserchangeform
	model=Customuser
	list_display = ['email','username','mob','clg']

admin.site.register(Customuser,Customuseradmin)	