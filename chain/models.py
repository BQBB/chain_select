import uuid

from django.db import models


class Manufacture(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.name}"


class Model(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.name}"


class Price(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="prices")
    price = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.price}"


class Product(models.Model):
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name="products")

    def __str(self):
        return f"{self.price.model.manufacture} - {self.price.model} - {self.price}"
