from django.db import models

# Create your models here.
class Diabetes(models.Model):
    Glocuse = models.FloatField(max_length =10)
    BMI = models.FloatField(max_length =10)
    Pressure = models.FloatField(max_length=10)

    def __str__(self) :
        return f' ${self.Glocuse}'