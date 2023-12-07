from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service
from todolist_app.models import TaskPerDay
from users.models import User


class TaskPerDayService(Service):
	user = forms.IntegerField()

	def process(self):
		user = User.objects.get(id=self.cleaned_data['user'])
		return TaskPerDay.objects.filter(user=user)
