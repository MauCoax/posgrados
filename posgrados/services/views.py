from django.contrib.auth.models import User
from .serializers import UserSerializer, UsuariosSerializer
from rest_framework import status, viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
#
@api_view(['POST'])
    def crear_usuario(request):
	    if request.method=='POST':
		    serializer=UsuariosSerializer(data=request.data)
		    print(request.data)
		    if serializer.is_valid():
			    serializer.save()
			    return Response(serializer.data, status=status.HTTP_201_CREATED)
 		    else:
			    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
