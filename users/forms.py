from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import Customuser


class Customusercreationform(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model =Customuser
		#fields = UserCreationForm.Meta.fields+('age',)
		fields=('username','clg','email','mob',)

class Customuserchangeform(UserChangeForm):

	class Meta:
		model=Customuser
		# fields=UserChangeForm.Meta.fields		
		fields=('username','clg','email','mob',)

