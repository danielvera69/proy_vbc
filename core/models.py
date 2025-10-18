from django.db import models
from django.contrib.auth.models import User

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    ruc = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default = True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
      
    def __str__(self):
        return f"{self.name} - {self.ruc}"
    
    