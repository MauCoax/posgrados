from django.contrib.auth.models import User, Group
from rest_framework import serializers


from .models import Usuario2, Rol,Permiso, RolPermiso, Noticia, Aspirante

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name')

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario2
        fields= '__all__'
        extra_kwargs ={'contrasena': {'write_only': True, 'required': True}}


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'


class RolPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolPermiso
        fields = '__all__'


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'


class AspiranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aspirante
        fields = '__all__'