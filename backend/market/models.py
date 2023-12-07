from django.db import models

# Create your models here.


class ProductCategory(models.Model):
	category = models.CharField()

class Product(models.Model):
	name = models.CharField()
	description = models.TextField(blank=True,null=True)
	category = models.ForeignKey(to=ProductCategory,on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	img = models.ImageField(upload_to='backend/imges/%Y/%m/%d/')