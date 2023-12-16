from django.db import models

from users.models import User


# Create your models here.

class Message(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Чат"
		verbose_name_plural = "Чат"

	def __str__(self):
		return self.author.username

	def last_10_messages():
		return Message.objects.order_by('-timestamp').all()[:10]
