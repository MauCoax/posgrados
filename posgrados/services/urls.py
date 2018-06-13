from django.conf.urls import url, include
from rest_framework import routers
from services.views import *

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'usuario',views.)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^usuarios/$', crear_usuario, name='crear_usuario'),
]