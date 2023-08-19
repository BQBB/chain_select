from django.contrib import admin

from chain.models import Manufacture, Model, Price, Product

admin.site.register(Manufacture)
admin.site.register(Model)
admin.site.register(Price)
admin.site.register(Product)
