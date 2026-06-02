from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        ordering = ['-fecha_registro']
        db_table = 'website_registro' #Se busca directamente en esta tabla de la base de datos

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.email} - {self.ciudad} - {self.telefono}"