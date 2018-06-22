from django.contrib.auth.models import User
from .serializers import UserSerializer, UsuariosSerializer
from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


#

class UsuarioViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'
    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializer

@api_view(['POST', 'GET'])
def crear_usuario(request):
    if request.method == 'GET':
        propiedad = Usuario.objects.all()
        serializer = UsuariosSerializer(propiedad, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UsuariosSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
