from django import forms
from service_objects.services import Service
from todolist_app.models import TaskPerWeek
from users.models import User


class TaskPerWeekService(Service):
	user = forms.IntegerField()

	def process(self):
		user = User.objects.get(id=self.cleaned_data['user'])
		return TaskPerWeek.objects.filter(user=user)
