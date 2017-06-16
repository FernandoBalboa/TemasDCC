from django.shortcuts import render
from models import *
# Create your views here.

def showTeacherTopics(request):
    teachers = Teacher.objects.all()
    
    return render(request, 'teacher_topics.html', {'teachers': teachers})
    