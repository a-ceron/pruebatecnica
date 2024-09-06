from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from . import serializers
from . import models


@api_view(['GET', 'POST'])
def users(request: 'request'):
    try:
        if request.method == 'GET':
            usuarios = models.Usuarios.objects.all()
            userserializer = serializers.UsuariosSerializer(usuarios, many=True)
            return Response(userserializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            userserializer = serializers.UsuariosSerializer(data=request.data)
            if userserializer.is_valid():
                userserializer.save()
                return Response(userserializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as e:
        return Response(f"Error: {e}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def user(request: 'request', iduser: 'int'):
    try:
        if request.method == 'GET':
            user = models.Usuarios.objects.filter(pk=iduser).first()
            userserializer = serializers.UsuariosSerializer(user)
            return Response(userserializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            user = models.Usuarios.objects.filter(pk=iduser).first()
            userserializer = serializers.UsuariosSerializer(user, data=request.data)
            if userserializer.is_valid():
                userserializer.save()
                return Response(userserializer.data, status=status.HTTP_200_OK)
            else:
                return Response(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            user = models.Usuarios.objects.filter(pk=iduser).first()
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as e:
        return Response(f"Error {e}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
