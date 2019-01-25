from django.contrib import admin

# Register your models here.

from .models import dhishnyadb
	
class Disp(admin.ModelAdmin):
	model=dhishnyadb
	list_display=['id','name','email','phone','college','date_creating']


admin.site.register(dhishnyadb,Disp) 