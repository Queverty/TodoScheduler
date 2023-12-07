from service_objects.services import Service
from market.models import Product

class ProductQuerySetGetService(Service):

	def process(self):
		return Product.objects.all()