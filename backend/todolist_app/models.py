
from django.db import models

from users.models import User
from django.utils import timezone


# Create your models here.
def end_of_week():
	today = timezone.now().date()
	start_of_week = today - timezone.timedelta(days=today.weekday())
	end_of_week = start_of_week + timezone.timedelta(days=6)
	return end_of_week


def end_of_month():
	today = timezone.now().date()
	start_of_month = today.replace(day=1)
	next_month = start_of_month.replace(day=28) + timezone.timedelta(days=4)
	end_of_month = next_month - timezone.timedelta(days=next_month.day)
	return end_of_month


def today():
	return timezone.now().date


class BaseTask(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField()
	is_completed = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateField(null=True, auto_now_add=True, verbose_name='Дата создания')
	updated_at = models.DateField(auto_now=True, verbose_name='Дата обновления')


class TaskPerDay(BaseTask):
	due_date = models.DateField(default=today)

	class Meta:
		verbose_name = "Задача на день"
		verbose_name_plural = "Задачи на день"


class TaskPerWeek(BaseTask):
	due_date = models.DateField(default=end_of_week)

	class Meta:
		verbose_name = "Задача на неделю"
		verbose_name_plural = "Задачи на неделю"


class TaskPerMonth(BaseTask):
	due_date = models.DateField(default=end_of_month)

	class Meta:
		verbose_name = "Задача на месяц"
		verbose_name_plural = "Задачи на месяц"


class TaskPerYear(BaseTask):
	due_date = models.DateField(default=timezone.now().date().replace(month=12, day=31))

	class Meta:
		verbose_name = "Задача на год"
		verbose_name_plural = "Задачи на год"


