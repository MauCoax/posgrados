from django.contrib.auth.models import User, Group, Permission, PermissionsMixin
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer, ImgSerializer,RolUsuariosSerializer,PasosSerializer,ProcedimientosSerializer,DocentesSerializer,User1Serializer, PermisionsMixinSerializer,  NoticiaSerializer, AspiranteSerializer, GroupSerializer, PermisionsSerializer
from rest_framework import status, viewsets, generics, mixins
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .models import  Noticia, Aspirante,Image, Docente, Pasos ,Procedimiento
from rest_framework.authtoken.models import Token
import json


class PermissionMixinAPICreate(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = (AllowAny,)
    lookup_field = 'id'
    serializer_class = PermisionsMixinSerializer

    def get_queryset(self):
        return PermissionsMixin.objects.all()

    def post(self, request , *args, **kwargs):
        return self.create(request , *args, **kwargs)

@api_view(['POST','GET'])
@permission_classes((AllowAny, ))
#@authentication_classes((TokenAuthentication, ))
def asignarrol(request,id=None,id2=None):
    try:
        rol=Group.objects.get(id=id)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='POST':
        try:
            rol.user_set.add(id2)
            #rol.objects.save()
            return Response(status=status.HTTP_201_CREATED)
        except Group.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes((AllowAny, ))
#@authentication_classes((TokenAuthentication, ))
def rolusuarios(request, id=None):
    try:
        rol=Group.objects.get(id=id)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        rol.get_user.all()
        serializer = RolUsuariosSerializer(rol)
        return Response(serializer.data)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class PermissionsAPICreate(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = (AllowAny,)
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    serializer_class = PermisionsSerializer

    def get_queryset(self):
        return Permission.objects.all()

    def post(self, request , *args, **kwargs):
        return self.create(request , *args, **kwargs)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self,request,*args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer = User1Serializer(user, many=False)
        return Response({'token': token.key, 'user': serializer.data})


class GroupAPICreateView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes = (AllowAny,)
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Usuario2APICreateView(mixins.CreateModelMixin,generics.ListAPIView):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    #permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self, request,id=None, *args, **kwargs):

        return self.create(request, *args, **kwargs)


class NoticiaAPICreate(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = (AllowAny,)
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

    def post(self, request , *args, **kwargs):
        json_data=json.loads(request.body)
        nombre=json_data["nombre_aspirante"]
        user=User.objects.create()
        user.first_name=nombre
        user.objects.save()

        return self.create(request , id=user.id, *args, **kwargs)


@api_view(['GET','POST'])
@permission_classes((AllowAny, ))
def imageApi(request):
    if request.method=='GET':
        imagenes=Image.objects.all()
        serializer=ImgSerializer(imagenes, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer =ImgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ruta=str(Image.objects.latest('img'))
            print(ruta)

            return Response(ruta, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocenteViewSet(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id_docente'
    serializer_class = DocentesSerializer

    def get_queryset(self):
        return Docente.objects.all()

class PasosApiCreate(generics.ListCreateAPIView):
    lookup_field = 'id_paso'
    serializer_class = PasosSerializer

    def get_queryset(self):
        return Pasos.objects.all()

class PasosApiCreateRetrive(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id_paso'
    serializer_class = PasosSerializer

    def get_queryset(self):
        return Pasos.objects.all()


class ProcedimientoApiCreate( generics.ListCreateAPIView):
    lookup_field = 'id_procedimiento'
    serializer_class = ProcedimientosSerializer

    def get_queryset(self):
        return Procedimiento.objects.all()

class ProcedimientoApiCreateRetrive( generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id_procedimiento'
    serializer_class = ProcedimientosSerializer

    def get_queryset(self):
        return Procedimiento.objects.all()



