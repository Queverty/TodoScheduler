from django.contrib.auth.models import AbstractUser
from django.db import models

from market.models import Product


# Create your models here.

class User(AbstractUser):
	email = models.EmailField(max_length=254, unique=True)
	balance = models.PositiveIntegerField(default=0)
	points = models.PositiveIntegerField(default=0)
	rank = models.PositiveIntegerField(default=999)

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

class Inventory(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	product = models.ForeignKey(Product,on_delete=models.CASCADE)

	def __str__(self):
		return f'Предмет пользователя - {self.user}'
	class Meta:
		verbose_name = "Инвентарь"
		verbose_name_plural = "Инвентарь"