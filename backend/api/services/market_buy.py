from django import forms
from service_objects.services import Service
from market.models import Product
from users.models import User, Inventory


class ProductBayGetService(Service):
	user_id = forms.IntegerField()
	product_id = forms.IntegerField()
	def process(self):
		return self.bay()

	def bay(self):
		user = self.get_user
		product = self.get_product
		if user.balance >= product.price:
			inv = Inventory.objects.create(user=user,product=product,quantity=1)
			user.balance -= product.price
			user.save()
			return 'Вы успешно купили товар!'
		else:
			return  'У вас не достаточно средств на балансе!'


	@property
	def get_user(self):
		return User.objects.get(id=self.cleaned_data['user_id'])
	@property
	def get_product(self):
		return Product.objects.get(id=self.cleaned_data['product_id'])