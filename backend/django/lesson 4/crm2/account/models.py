from django.db import models

# Create your models here.
# aca voy a crear la base de validators


class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)  # atributo vharfield es string
	phone = models.CharField(max_length=200, null=True) # queda null por default importar sin defaut vlaue
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True) # se crea automatico auto_now_add


	def __str__(self):
		return self.name   # ver el nombre en la base de datos

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			)

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	#customer =
	#product =
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
