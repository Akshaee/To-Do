from django.http import HttpResponse
from django.shortcuts import render
from to_do.models import Task
from django.utils import timezone

def home(request):
  tasks = Task.objects.filter(is_completed=False).order_by('-updated_time')
  completed_tasks = Task.objects.filter(is_completed = True)
  context = {
    'tasks' : tasks,
    'completed_tasks': completed_tasks
  } 
  return render(request, 'home.html', context)