from django.urls import path
from.import views

urlpatterns=[
    path('',views.projects,name="projects"),
    # path('',views.templates,name="templates"),

    # path('nevbar/',views.nevbar,name='nevabr'),
    # path('register/',views.registerPage,name='register'),
    # path('login/',views.loginPage,name='login'),
    # path('feedback/',views.Feedback,name='feedback'),
    path('home/',views.index,name='index'),
    # path('contact/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('todo/',views.todo,name='todo'),
    path('contact/',views.contact,name='contact'),
    

    
    
    
    
    
] 
