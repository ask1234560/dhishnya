from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import Customusercreationform


# Create your views here.

class Signupview(CreateView):
	form_class=Customusercreationform
	success_url=reverse_lazy('login')
	template_name='signup.html'
