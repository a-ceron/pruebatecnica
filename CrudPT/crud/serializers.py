from . import models
from rest_framework import serializers

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuarios
        fields = '__all__'