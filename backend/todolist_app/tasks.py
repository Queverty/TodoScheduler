from celery import shared_task
from django.utils.timezone import now




@shared_task
def TaskPerDay_deleted():
	from todolist_app.models import TaskPerDay
	expired_objects = TaskPerDay.objects.filter(due_date__lte=now())
	expired_objects.delete()

@shared_task
def TaskPerMonth_deleted():
	from todolist_app.models import TaskPerMonth
	expired_objects = TaskPerMonth.objects.all().delete()

@shared_task
def TaskPerWeek_deleted():
	from todolist_app.models import TaskPerWeek
	expired_objects = TaskPerWeek.objects.all()
	expired_objects.delete()
