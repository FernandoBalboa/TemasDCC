from django.shortcuts import render, redirect
from models import *
# Create your views here.

def showTeacherTopics(request):
    teachers = Teacher.objects.all()
    
    return render(request, 'teacher_topics.html', {'teachers': teachers})
    
def index(request):
    return redirect('/teacher_topics')