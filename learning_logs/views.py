from ast import Return
from django.shortcuts import render



def index(request):
    """Home Page"""
    return render(request, 'learning_logs/index.html',)

def exercises(request):
    """About student page"""
    return render(request, 'learning_logs/exercises.html',)

def about(request):
    """exercises [age"""
    return render(request, 'learning_logs/about.html' )

def exer1(request):
    """exercise 1 page"""
    return render(request, 'learning_logs/exer1.html')

def exer2(request):
    """exercise 2 page"""
    return render(request, 'learning_logs/exer2.html')

def exer3(request):
    """exercise 3 page"""
    return render(request, 'learning_logs/exer3.html')

def exer5(request):
    """exercise 5 page"""
    return render(request, 'learning_logs/exer5.html')

def exer6(request):
    """exercise 6 page"""
    return render(request, 'learning_logs/exer6.html')

def exer7(request):
    """exercise 7 page"""
    return render(request, 'learning_logs/exer7.html')

def exer8(request):
    """exercise 8 page"""
    return render(request, 'learning_logs/exer8.html')

def exer9(request):
    """exercise 9 page"""
    return render(request, 'learning_logs/exer9.html')

def exer10(request):
    """exercise 10 page"""
    return render(request, 'learning_logs/exer10.html')



    


