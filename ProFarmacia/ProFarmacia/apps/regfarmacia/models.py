from django.db import models

# Create your models here.
class Farmacias(models.Model):
	ID_Usuario=models.CharField(max_length=30,primary_key=True,unique=True)
	Name_Farmacia=models.CharField(max_length=30)
	Ubicacion=models.CharField(max_length=100,null=False)
	Email=models.CharField(max_length=100)
	Password = models.CharField(max_length=100,null=False)

class Inventarios(models.Model):
	Name_med=models.CharField(max_length=100)
	Cantidad=models.IntegerField(max_length=10,null=False)
	Costo=models.FloatField(max_length=10,null=False)
	ID_Usuario=models.CharField(max_length=30)
	Categoria = models.CharField(max_length=50)

class ReporteVentas(models.Model):
	ID_Usuario=models.CharField(max_length=30)
	Name_med=models.CharField(max_length=100)
	CantidadV=models.IntegerField(max_length=10,null=False)
	Total=models.FloatField(max_length=10,null=False)
	Fecha=models.DateField(auto_now=True)

class ContadorBusq(models.Model):
	Name_med=models.CharField(max_length=100,primary_key=True)
	Contador=models.IntegerField(max_length=100)
	
