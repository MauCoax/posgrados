from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from .services import views


router = routers.SimpleRouter()
router.register(r'usuarios', views.UsuarioViewSet, 'user-list')
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^services/', include('services.urls')),
    url(r'^', include(router.urls)),
    url(r'^services/usuarios/(?P<pk>\d+)/$', views.UsuarioViewSet.as_view, name='usuario-list'),
    url(r'^services/usuarios/$', views.UsuarioAPICreateView.as_view(), name='usuario-create'),
    url(r'^services/roles/$', views.RolAPICreate.as_view(), name='roles-create'),
]