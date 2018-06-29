from django.contrib.auth.models import User, Group, Permission, PermissionsMixin
from rest_framework import serializers


from .models import Usuario2, Rol,Permiso, RolPermiso, Noticia, Aspirante


class RolUsuariosSerializer(serializers.ModelSerializer):

    users_list = serializers.SerializerMethodField()
    def get_users_list(self, instance):
        users=[]
        u=instance.users.get_queryset()
        for i in u:
            users.append(i.desc)
        return users

    class Meta:
        model = Group
        fields =('users_list', )




class PermisionsMixinSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionsMixin
        fields = '__all__'


class PermisionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

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