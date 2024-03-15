from django.db import models

# Create your models here.

class autor (models.Model): 
    nombre = models.CharField(max_length=65)
    def __str__(self): 
        return self.nombre 

class libro(models.Model): 

    nombreAutor = models.ForeignKey(autor,on_delete=models.PROTECT) 
    fecha = models.DateField()
    descripcion = models.TextField()
    nombreLibro = models.CharField(max_length=50) 
    def __str__(self):
        return self.nombreLibro