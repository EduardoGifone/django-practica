from rest_framework import serializers

from base.models import *

class OficinaSerializer (serializers.ModelSerializer):
  class Meta:
    model = Oficina
    fields = [
      'nombre'
    ]

class UsuarioSerializer (serializers.ModelSerializer):
  oficina = OficinaSerializer()
  class Meta:
    model = Usuario
    fields = '__all__'