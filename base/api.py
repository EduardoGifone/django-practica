from rest_framework import viewsets

from base.models import *

from base.serializers import *

class OficinaViewSet (viewsets.ModelViewSet):
  serializer_class = OficinaSerializer
  queryset = Oficina.objects.all()

class UsuarioViewSet (viewsets.ModelViewSet):
  serializer_class = UsuarioSerializer
  queryset = Usuario.objects.all()