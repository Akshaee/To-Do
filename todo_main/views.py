from django.http import HttpResponse
from django.shortcuts import render
from to_do.models import Task
from django.utils import timezone
from to_do.utils import old_task_history

def home(request):
  old_task_history()
  tasks = Task.objects.filter(is_completed=False).order_by('-updated_time')
  completed_tasks = Task.objects.filter(is_completed = True)
  context = {
    'tasks' : tasks,
    'completed_tasks': completed_tasks
  } 
  return render(request, 'home.html', context)