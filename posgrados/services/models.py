from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
#





class Noticia (models.Model) :
    emcabezado = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=100)
    id_user = models.ForeignKey( User , models.SET_NULL,
    blank=True,
    null=True,)
    fecha = models.DateField(auto_now=True)
    imagen = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return str(self.emcabezado)


class Image(models.Model):
    img = models.ImageField(upload_to='uploads/{0}'.format("%d-%m-%y/%H_%M_%S"), default='static/f1.png')

    def __str__(self):
        return str(self.img)


class Aspirante (models.Model) :
    id_aspirante = models.AutoField(primary_key=True)
    nombreuser_aspirante = models.CharField(max_length=10)
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
    aceptado = models.BooleanField()
    id_user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, )
    id_val = models.ForeignKey('validacion', models.SET_NULL, blank=True, null=True, )

    def __str__(self):
                return str(self.nombre_aspirante)

class Docente(models.Model) :
    id_docente = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dui = models.CharField(max_length=10)
    genero = models.CharField(max_length=15)
    fecha_naci = models.DateField()
    telefono = models.CharField(max_length=15)
    movil = models.CharField(max_length=15)
    email = models.CharField(max_length=35)
    formacion = ArrayField(models.CharField(max_length=20),size=5)
    titulo = ArrayField(models.CharField(max_length=20),size=5)

    def __str__(self):
        return (self.nombre,self.apellido)

class Validacion (models.Model):
    id_codigo=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=8)
    vigencia= models.DateField()

class Procedimiento(models.Model):
    id_procedimiento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return(self.nombre)

class Pasos(models.Model):
    id_paso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    id_proceimiento = models.ForeignKey('Procedimiento', models.SET_NULL, blank=True, null=True,)
    orden = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return(self.nombre)

