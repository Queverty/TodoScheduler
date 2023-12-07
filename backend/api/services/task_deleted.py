from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service

from api.services.task_base_complited import task_complited
from todolist_app.models import TaskPerDay, BaseTask
from users.models import User


class TaskDeletedService(Service):

	task_id = forms.IntegerField()

	def process(self):
		return BaseTask.objects.get(id=self.cleaned_data['task_id']).delete()
