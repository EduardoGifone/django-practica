from django.urls import path, include

from rest_framework import routers

from base import api

router = routers.DefaultRouter()
router.register('oficinas', api.OficinaViewSet)
router.register('usuarios', api.UsuarioViewSet)


app_name = 'base'
urlpatterns = [
  #api
  path('api/base/', include(router.urls))
]