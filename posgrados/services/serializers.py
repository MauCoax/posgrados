from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Usuario

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields= '__all__'
        extra_kwargs ={'contrasena': {'write_only': True, 'required': True}}
