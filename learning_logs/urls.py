"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name= 'learning_logs'

urlpatterns = [
    #Home page
    path('',views.index, name='index'),
        
    path('exercises', views.exercises, name='exercises'),

    path('about',views.about, name='about'),
    
    path('exer1',views.exer1, name='exer1'),
    
    path('exer2',views.exer2, name='exer2'),

    path('exer3',views.exer3, name='exer3'),

    path('exer5',views.exer5, name='exer5'),

    path('exer6',views.exer6, name='exer6'),

    path('exer7',views.exer7, name='exer7'),

    path('exer8',views.exer8, name='exer8'),
    
    path('exer9',views.exer9, name='exer9'),
    
    path('exer10',views.exer10, name='exer10'),
        
]

urlpatterns += staticfiles_urlpatterns()