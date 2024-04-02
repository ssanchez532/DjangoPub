from django.db import models

# Create your models here.

opciones_documento = [
    ('CC', "Cédula de Ciudadanía"),
    ('Pasaporte', "Pasaporte"),
    ('CedulaExtranjeria', "Cédula de Extranjería"),
]

opciones_franquisia = [
    ('Visa', "Visa"),
    ('MasterCard', "MasterCard"),
    ('AmericanExpress', "American Express"),
]

class Datos_Usuario(models.Model):
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)  # Permitir campos opcionales
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)  # Permitir campos opcionales
    documento = models.CharField(max_length=50, choices=opciones_documento)  # Utilizar CharField y definir las opciones como tuplas
    numero_documento = models.IntegerField()
    correo = models.EmailField()
    celular = models.CharField(max_length=20)  # Utilizar CharField para el número de celular
    ciudad = models.CharField(max_length=60)
    direccion = models.TextField()
    ingresos = models.IntegerField()
    actividad = models.CharField(max_length=50)
    franquicia = models.CharField(max_length=50, choices=opciones_franquisia)  # Utilizar CharField y definir las opciones como tuplas
    def __str__(self):
        return self.correo
