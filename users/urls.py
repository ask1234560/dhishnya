from django.urls import path

from .views import Signupview
from django.views.generic.base import TemplateView

urlpatterns = [
path('signup/',Signupview.as_view(),name='signup'),
path('notlogged/',TemplateView.as_view(template_name='notlogd.html'),name='notlog'),

] 

