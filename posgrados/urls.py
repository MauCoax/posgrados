from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from .services import views
from rest_framework.authtoken.views import ObtainAuthToken
from django.conf.urls.static import static




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^services/usuarios/(?P<id>(\d+))/$', views.Usuario2APICreateView.as_view(), name='usuario-create'),
    url(r'^services/asignaroless/(?P<id>(\d+))/usuario/(?P<id2>(\d+))/$', views.asignarrol, name='roles-usuarios'),
    url(r'^services/roles/$', views.GroupAPICreateView.as_view(), name='roles-create'),
    url(r'^services/permisos/$', views.PermissionsAPICreate.as_view(), name='permisos-create'),
    url(r'^services/rolpermisos/$', views.PermissionMixinAPICreate.as_view(), name='rolpermisos-create'),
    url(r'^services/noticia/$', views.NoticiaAPICreate.as_view(), name='noticia-create'),
    url(r'^services/usuarios/$', views.Usuario2APICreateView.as_view(), name='usuario-create'),
    url(r'^services/aspirante/$', views.AspiranteAPICreate.as_view(), name='aspirante-create'),
    url(r'^services/aspirante/(?P<id_aspirante>(\d+))/$', views.AspiranteAceptado, name='aspirante-create'),
    url(r'^auth/', views.CustomObtainAuthToken.as_view()),
    url(r'^services/rol/(?P<id>(\d+))/$', views.rolusuarios, name='roles-usuarios'),
    url(r'^imagen/$', views.imageApi, name='imagen'),
    url(r'^services/docentes/$',views.DocenteViewSet.as_view(), name='docentes-create'),
    url(r'^services/docentes/(?P<id_docente>(\d+))/$',views.DocenteViewSetRetrive.as_view(), name='docentes-create'),
    url(r'^services/pasos/(?P<id_paso>(\d+))/$',views.PasosApiCreateRetrive.as_view(), name='pasos-create'),
    url(r'^services/pasos/$',views.Pasosnuevos, name='pasos-create'),
    url(r'^services/procedimiento/(?P<id_procedimiento>(\d+))/$',views.ProcedimientoApiCreateRetrive.as_view(), name='procedimiento-create'),
    url(r'^services/procedimiento/$',views.ProcedimientoApiCreate.as_view(), name='procedimiento-create'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
