from django.shortcuts import render

# Create your views here.

def showTeacherTopics(request):
    return render(request, 'teacher_topics.html')
    