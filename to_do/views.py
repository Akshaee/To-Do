from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TaskHistory
from django.utils import timezone
from django.contrib import messages
from datetime import date
from .utils import old_task_history
from datetime import timedelta

def  add_task(request):
  task = request.POST.get('task', '').strip()
  if not task:
    messages.warning(request, "Please enter a task before submitting.")
    return redirect('home')
  Task.objects.create(task=task)
  messages.success(request, "Task added successfully!")
  return redirect('home')
  
def mark_as_done(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.mark_completed()
  messages.success(request, "Marked as completed")
  return redirect('home')

def mark_as_undone(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.is_completed = False
  task.completed_at = timezone.now()
  task.save()
  messages.success(request, "Remove from completed task")
  return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        new_task = request.POST.get('task', '').strip()

        # EMPTY VALIDATION
        if not new_task:
            messages.warning(request, "Task cannot be empty. Please enter something.")
            # Stay on the edit page
            return render(request, 'edit_task.html', {'get_task': get_task})

        # VALID -> UPDATE
        get_task.task = new_task
        get_task.save()
        messages.success(request, "Task updated successfully!")
        return redirect('home')

    # GET request -> show edit page
    return render(request, 'edit_task.html', {'get_task': get_task})

def delete_task(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.delete()
  messages.warning(request, "Task deleted")      
  return redirect('home')

def history(request):
    today = date.today()

    yesterday = today - timedelta(days=1)
    last_week = today - timedelta(weeks=1)
    last_month = today - timedelta(days=30)
    last_3_months = today - timedelta(days=90)
    last_6_months = today - timedelta(days=180)
    last_year = today - timedelta(days=365)

    history_tasks = TaskHistory.objects.all().order_by('-date')

    context = {
        "sections": [
            ("Yesterday", history_tasks.filter(date=yesterday)),
            ("Last Week", history_tasks.filter(date__range=(last_week, yesterday - timedelta(days=1)))),
            ("Last Month", history_tasks.filter(date__range=(last_month, last_week - timedelta(days=1)))),
            ("Last 3 Months", history_tasks.filter(date__range=(last_3_months, last_month - timedelta(days=1)))),
            ("Last 6 Months", history_tasks.filter(date__range=(last_6_months, last_3_months - timedelta(days=1)))),
            ("Last 1 Year", history_tasks.filter(date__range=(last_year, last_6_months - timedelta(days=1)))),
            ("Lifetime", history_tasks.filter(date__lt=last_year)),
        ]
    }

    return render(request, 'history.html', context)
