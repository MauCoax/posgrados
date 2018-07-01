from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
#


class Usuario2 (models.Model) :
     #  rolid = models.ForeignKey('Rol',on_delete=models.CASCADE)
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=15)
    rol_id = models.ForeignKey('Rol', models.SET_NULL,
    blank=True,
    null=True,)
    def __str__(self):
        return str(self.nombre)


class Noticia (models.Model) :
    emcabezado = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=100)
    id_user = models.ForeignKey( User , models.SET_NULL,
    blank=True,
    null=True,)
    fecha = models.DateField(auto_now=True)
    imagen = ArrayField(models.CharField(max_length=250, blank=True), size=10)

    def __str__(self):
        return str(self.emcabezado)


class Image(models.Model):
    img = models.ImageField(upload_to='uploads/{0}'.format("%d-%m-%y/%H_%M_%S"), default='uploads/f1.png')

    def __str__(self):
        return str(self.img)


class Aspirante (models.Model) :
    id_aspirante = models.AutoField(primary_key=True)
    nombre_aspirante = models.CharField(max_length=20)
    apellido_aspirante = models.CharField(max_length=20)
    contrasena_aspirante = models.CharField(max_length=10)
    dui = models.CharField(max_length=9)
    genero = models.CharField(max_length=9)
    fechas_nac = models.DateField()
    t_fijo = models.CharField(max_length=10)
    t_movil = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    titulo_pre = models.CharField(max_length=30)
    institucion = models.CharField(max_length=30)
    f_expedicion = models.DateField()
    municipio = models.CharField(max_length=50)
    lugar_trab = models.CharField(max_length=50)
    programa = models.CharField(max_length=50)
    id_user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, )
    id_val = models.ForeignKey('validacion', models.SET_NULL, blank=True, null=True, )

    def __str__(self):
                return str(self.nombre_aspirante)


class Validacion (models.Model):
    id_codigo=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=8)
    vigencia= models.DateField()


class Rol(models.Model):

    nombre = models.CharField(max_length=50)
    rolid = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.nombre)
#
#     def __str__(self):
#         return str(self.nombre)
#


class Permiso(models.Model):
     permisoId = models.AutoField(primary_key=True)
     nombre_permiso = models.CharField(max_length=50)
     codigo_permiso = models.CharField(max_length=50)

     def __str__(self):
         return str(self.nombre_permiso)
#
#     def __str__(self):
#         return str(self.nombre)
#
# class PermisoUsuario(models.Model):
#     permisoUsuarioId=models.IntegerField(primary_key=True)
#     usuarioId=models.ForeignKey('Usuario')
#     permisoId=models.ForeignKey('Permiso')
#

class RolPermiso(models.Model):
     rolPermisoId= models.AutoField(primary_key=True)
     rolId=models.ForeignKey('Rol', models.SET_NULL,
     blank=True,
     null=True,)
     permisoId=models.ForeignKey('Permiso',models.SET_NULL,
     blank=True,
     null=True,)

     def __str__(self):
         return str(self.rolPermisoId)

