from django.shortcuts import render,redirect
import django
# Create your views here.
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.shortcuts import HttpResponseRedirect
from .models import dhishnyadb
from users.models import Customuser
#from django.contrib.auth.decorators import login_required
# from django.urls import reverse




class Homepageview(TemplateView):
        template_name='home.html'


# class Game(TemplateView): 
#         def check(request):
#                 print(request.user)    

#         template_name='index.html'      

class Game(TemplateView):
        template_name='index.html'



# @csrf_exempt
# def game(request):
#      data={}   
#      print(request.user) 
#      return redirect(Dhi)
#      # render('index.html')
#      # data["status"]=3
#      # data["repeat"]=0
#      # return HttpResponse(json.dumps(data), content_type="application/json") 




#@login_required
@csrf_exempt
def ver(request):
      data={}
      status=203;

      if request.is_ajax():
              username=request.user
              userAnswer=int(request.POST.get("answer", ""))
              question=int(request.POST.get("question", ""))
              #print(userAnswer)
              #print(question)
              repeat=0        
              answers={'1': 3, '2': 4, '3': 3, '4': 1, '5':3, '6':1, '7':4, '8':4, '9':3, '10':2}     
              status=201
              if True:
                      print(question, userAnswer, answers[str(question)])
                      #print(type(question), type(userAnswer), type(answers[str(question)]))
                      print(answers[str(question)]==userAnswer)

                      if request.session.has_key(str(question)):
                              repeat=10
                      if(answers[str(question)]==userAnswer):
                              status=200
                      else:
                              status=201

                      if question==10 and status==200:
                                        # user=request.user
                                        user=Customuser.objects.get(username=request.user)
                                        # query=Login.objects.get(user=user)
                                        # name=query.username
                                        # college=query.clg
                                        # phone=query.mob
                                        # email=query.email
                                        college=user.clg
                                        phone=user.mob
                                        email=user.email
                                        name=user.username
                                        # print(type(name),name,college,phone,email)
                                        try:
                                                dhishnyadb.objects.create(name=name, college=college, phone=phone, email=email)
                                        except:
                                                pass;
                                                        
              # print(repeat)
      data["status"]=status
      data["repeat"]=repeat
      request.session[str(question)] = 10
      return HttpResponse(json.dumps(data), content_type="application/json")  



