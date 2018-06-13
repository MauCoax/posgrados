from django.db import models

# Create your models here.
#

class Usuario (models.Model) :
     #  rolid = models.ForeignKey('Rol',on_delete=models.CASCADE)
    nombre = models.CharField(max_length=25)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=15)
    def __str__(self):
        return str(self.nombre)


# class Rol(models.Model):

#     nombre = models.CharField(max_length=25)
#     rolid = models.AutoField(primary_key=True)
#
#     def __str__(self):
#         return str(self.nombre)
#
# class Permiso(models.Model):
#     permisoId = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=25)
#     codigo = models.CharField(max_length=25)
#
#     def __str__(self):
#         return str(self.nombre)
#
# class PermisoUsuario(models.Model):
#     permisoUsuarioId=models.IntegerField(primary_key=True)
#     usuarioId=models.ForeignKey('Usuario')
#     permisoId=models.ForeignKey('Permiso')
#
# class RolPermiso(models.Model):
#     rolPermisoId= models.AutoField(primary_key=True)
#     rolId=models.ForeignKey('Rol')
#     permisoId=models.ForeignKey(Permiso)
#
