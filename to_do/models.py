from django.db import models
from django.utils import timezone

class Task(models.Model):
  task = models.CharField(max_length=250)
  is_completed = models.BooleanField(default=False)
  completed_at = models.DateTimeField(null=True, blank=True)
  created_time = models.DateTimeField(auto_now_add=True)
  updated_time = models.DateTimeField(auto_now=True)
  
  def mark_completed(self):
    self.is_completed = True
    self.completed_at = timezone.now()
    self.save()
    
  def __str__(self):
    return self.task
  
class TaskHistory(models.Model):
  task = models.CharField(max_length=255)
  is_completed = models.BooleanField(default=False)
  date = models.DateField()
