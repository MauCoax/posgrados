from django.contrib.auth.models import User, Group, Permission
from rest_framework.permissions import IsAuthenticated , AllowAny


from .serializers import UserSerializer, UsuariosSerializer, RolSerializer, PermisoSerializer, RolPermisoSerializer, NoticiaSerializer, AspiranteSerializer, GroupSerializer, PermisionsSerializer
from rest_framework import status, viewsets, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario2, Rol , Permiso, RolPermiso, Noticia, Aspirante

class PermissionsAPICreate(mixins.CreateModelMixin, generics.ListAPIView):

    permission_classes = (AllowAny,)
    lookup_field = 'id'
    serializer_class = PermisionsSerializer

    def get_queryset(self):
        return Permission.objects.all()

    def post(self, request , *args, **kwargs):
        return self.create(request , *args, **kwargs)


class GroupAPICreateView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Usuario2APICreateView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes = (AllowAny,)
    lookup_field = 'id'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UsuarioViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'
    queryset = Usuario2.objects.all()
    serializer_class = UsuariosSerializer


class UsuarioAPICreateView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'usuario_id'
    serializer_class = UsuariosSerializer

    def get_queryset(self):
        return Usuario2.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RolAPICreate(mixins.UpdateModelMixin, mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'rol_id'
    serializer_class = RolSerializer

    def get_queryset(self):
        return Rol.objects.all()

    def post(self, request , *args, **kwargs):
        return self.create(request , *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PermisosAPICreate(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'permisoId'
    serializer_class = PermisoSerializer

    def get_queryset(self):
        return Permiso.objects.all()

    def post(self, request , *args, **kwargs):
        return self.create(request , *args, **kwargs)


class RolPermisoAPICreate(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'rolpermisoId'
    serializer_class = RolPermisoSerializer

    def get_queryset(self):
        return RolPermiso.objects.all()

    def post(self, request , *args, **kwargs):
        return self.create(request , *args, **kwargs)


class NoticiaAPICreate(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        return Noticia.objects.all()

    def post(self, request , *args, **kwargs):
        return self.create(request , *args, **kwargs)


class AspiranteAPICreate(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = (AllowAny,)
    lookup_field = 'id_aspirante'
    serializer_class = AspiranteSerializer

    def get_queryset(self):
        return Aspirante.objects.all()

    def post(self, request , *args, **kwargs):
        return self.create(request , *args, **kwargs)