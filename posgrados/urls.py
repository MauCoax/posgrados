from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from .services import views
from rest_framework.authtoken.views import ObtainAuthToken




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^services/usuarios/$', views.Usuario2APICreateView.as_view(), name='usuario-create'),
    url(r'^services/asignaroless/(?P<id>(\d+))/usuario/(?P<id2>(\d+))/$', views.asignarrol, name='roles-usuarios'),
    url(r'^services/roles/$', views.GroupAPICreateView.as_view(), name='roles-create'),
    url(r'^services/permisos/$', views.PermissionsAPICreate.as_view(), name='permisos-create'),
    url(r'^services/rolpermisos/$', views.PermissionMixinAPICreate.as_view(), name='rolpermisos-create'),
    url(r'^services/noticia/$', views.NoticiaAPICreate.as_view(), name='noticia-create'),
    url(r'^services/usuarios2/$', views.Usuario2APICreateView.as_view(), name='usuario-create'),
    url(r'^services/aspirante/$', views.AspiranteAPICreate.as_view(), name='usuario-create'),
    url(r'^auth/', ObtainAuthToken.as_view()),
    url(r'^services/rol/(?P<id>(\d+))/$', views.rolusuarios, name='roles-usuarios'),


]