from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone

def  add_task(request):
  task = request.POST['task']
  Task.objects.create(task=task)
  return redirect('home')
  
def mark_as_done(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.mark_completed()
  return redirect('home')

def mark_as_undone(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.is_completed = False
  task.completed_at = timezone.now()
  task.save()
  return redirect('home')

def edit_task(request, pk):
  get_task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST':
    new_task = request.POST['task']
    get_task.task = new_task
    get_task.save()
    return redirect('home')
  else:
    context = {
      'get_task' : get_task,
    }
    return render(request, 'edit_task.html', context)

def delete_task(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.delete()
  return redirect('home')