from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from.models import*
# from.forms import OrderFrom
#  from.filters import orderFilter

projectList=[
    
    {
        'id':'1',
        'title':"Ecommerce website",
        'description':'Fully function ecommerce website'
    },
    {
        'id':'2',
        'title':"portfolio website",
        'description':'This was a project where I built out my portfolio'
    },
    {
       'id':'3',
        'title':"Social Network",
        'description':'Awesome open source peoject I am still working on' 
    },
]
def registerPage(request):
    form= UserCreationForm()
    
    if request.method=='post':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'projects/register.html',context)

# def registerPage(request):
#     context={}
#     return render(request,'projects/register.html',context)

    
    

def loginPage(request):
    context={}
    return render(request,'projects/login.html',context)
    
    

def projects(request):
    page='projects'
    number=10
    context={'page':page,'number':number,'project':projectList}
    return render(request,'projects/project.html',context)

 
def nevbar(request):
    return render(request,'projects/nevbar.html') 

def Feedback(request):
    return render(request,'projects/Feedback.html')  
 
def index(request):
    return render(request,'projects/index.html')

def home(request):
    return render(request,'projects/home.html')

def about(request):
    return render(request,'projects/about.html')

def todo(request):
    return render(request,'projects/todo.html')

def contact(request):
    return render(request,'projects/contact.html')