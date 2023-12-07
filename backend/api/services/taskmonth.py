from django import forms
from service_objects.services import Service
from todolist_app.models import TaskPerMonth
from users.models import User


class TaskPerMonthService(Service):
	user = forms.IntegerField()

	def process(self):
		user = User.objects.get(id=self.cleaned_data['user'])
		return TaskPerMonth.objects.filter(user=user)
