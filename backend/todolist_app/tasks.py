from celery import shared_task
from django.utils.timezone import now

from todolist_app.models import TaskPerDay, TaskPerWeek


@shared_task
def delete_expired_objects():
	expired_objects = TaskPerWeek.objects.filter(due_date__lte=now())
	expired_objects.delete()

