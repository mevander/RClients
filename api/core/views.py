from .models import *
from .serializers import *
from rest_framework import viewsets
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class EndClienteViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EndClienteSerializer
