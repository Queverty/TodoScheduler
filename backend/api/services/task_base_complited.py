# from django import forms
# from service_objects.fields import ModelField
# from service_objects.services import Service
# from todolist_app.models import TaskPerDay
# from users.models import User
#
#
# class TaskPerDayService(Service):
# 	user = forms.IntegerField()
#
# 	def process(self):
# 		user = User.objects.get(id=self.cleaned_data['user'])
# 		return TaskPerDay.objects.filter(user=user)
from users.models import User


def task_complited(task_type,task_id,user_id):
	task = task_type.objects.get(id=task_id)
	task.is_completed = True
	task.save()
	user = User.objects.get(id=user_id)
	user.balance += 10
	user.points += 50
	user.save()

