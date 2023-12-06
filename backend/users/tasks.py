from celery import shared_task
from django.utils.timezone import now

from .models import User


@shared_task
def calculate_rank():
	users = User.objects.order_by('-points')
	current_rank = 1
	for user in users:
		user.rank = current_rank
		user.save()
		current_rank += 1
