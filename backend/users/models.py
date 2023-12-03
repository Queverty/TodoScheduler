from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
	email = models.EmailField(max_length=254, unique=True)

	def __str__(self):
		return self.username

class Subscribe(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Подписчик",related_name='subscriber')
	author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Автор",related_name='author')

	def __str__(self):
		return f"Подписчик {self.user} - автор {self.author}"

	class Meta:
		verbose_name = 'Подписка'
		verbose_name_plural = 'Подписки'