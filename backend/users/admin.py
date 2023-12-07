from django.contrib import admin

from users.models import User, Subscribe, Inventory

# Register your models here.


admin.site.register(User)
admin.site.register(Subscribe)
admin.site.register(Inventory)