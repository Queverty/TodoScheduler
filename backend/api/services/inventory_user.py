from django import forms
from service_objects.services import Service
from users.models import User, Inventory


class InventoryGetService(Service):
	user_id = forms.IntegerField()

	def process(self):
		return self.get_inventory

	@property
	def get_user(self):
		return User.objects.get(id=self.cleaned_data['user_id'])

	@property
	def get_inventory(self):
		return Inventory.objects.filter(user=self.get_user)
