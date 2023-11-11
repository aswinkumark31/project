from django.shortcuts import render
from . models import *
from . forms import *

# Create your views here.

def index(request):
    pro=Task.objects.all()

    if request.method=="POST":

        if 'delete' in request.POST:
            key=request.POST.get('delete')
            fo=Task.objects.get(id=key)
            fo.delete()

            
    form_obj=Todo_form

    contest={}
    contest['pro']=pro
    contest['form_obj']=form_obj
    
    return render(request,'index.html',contest)




def home(request):
    pro=Task.objects.all()

    form_obj=Todo_form()

    if request.method=="POST":
        if 'save' in request.POST:
            form=Todo_form(request.POST)
            form.save()
            form_obj=Todo_form()

    context={}
    context['pro']=pro
    context['form_obj']=form_obj
    
    return render(request,'home.html',context)


