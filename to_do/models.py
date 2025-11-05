from django.db import models

class Task(models.Model):
  task = models.CharField(max_length=250)
  is_completed = models.BooleanField(default=False)
  created_time = models.DateTimeField(auto_now_add=True)
  updated_time = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.task
  

