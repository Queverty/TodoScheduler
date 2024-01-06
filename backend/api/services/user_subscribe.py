from django import forms
from service_objects.services import Service
from users.models import User, Inventory, Subscribe


class SubscribeService(Service):
	user_id = forms.IntegerField()
	author_id = forms.IntegerField()

	def process(self):
		return self.subcribe

	@property
	def get_user(self):
		return User.objects.get(id=self.cleaned_data['user_id'])

	@property
	def get_author(self):
		return User.objects.get(id=self.cleaned_data['author_id'])

	@property
	def subcribe(self):
		queryset = Subscribe.objects.create(author=self.get_author, user=self.get_user)
		queryset.save()
