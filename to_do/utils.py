from datetime import date
from .models import Task, TaskHistory

def old_task_history():
    today = date.today()

    # Use created_time, NOT completed_at
    old_tasks = Task.objects.exclude(created_time__date=today)

    history_objects = [
        TaskHistory(
            task=t.task,
            is_completed=t.is_completed,
            date=t.created_time.date()  # convert datetime → date
        )
        for t in old_tasks
    ]

    TaskHistory.objects.bulk_create(history_objects)
    old_tasks.delete()