from django.contrib.auth.models import User
from .serializers import UserSerializer, UsuariosSerializer, RolSerializer
from rest_framework import status, viewsets, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario2, Rol


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


#

class UsuarioViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'
    queryset = Usuario2.objects.all()
    serializer_class = UsuariosSerializer

class UsuarioAPICreateView(generics.CreateAPIView):
    lookup_field = 'usuario_id'
    serializer_class = UsuariosSerializer
    def get_queryset(self):
        return Usuario2.objects.all()
class RolAPICreate(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'rol_id'
    serializer_class = RolSerializer
    def get_queryset(self):
        return Rol.objects.all()
    def post(self, request , *args, **kwargs):
        return self.create(request , *args, **kwargs)