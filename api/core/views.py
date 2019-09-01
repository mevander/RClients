from rest_framework import viewsets
from .models import Cliente, Endereco
from .serializers import *


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class EndClienteViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EndClienteSerializer
