from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service

from api.services.task_base_complited import task_complited
from todolist_app.models import TaskPerDay
from users.models import User


class TaskPerDayComplitedService(Service):
	user_id = forms.IntegerField()
	task_id = forms.IntegerField()


	def process(self):
		return task_complited(task_type=TaskPerDay,
							  task_id=self.cleaned_data['task_id'],
							  user_id=self.cleaned_data['user_id'])
