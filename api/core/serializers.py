from .models import Cliente, Endereco
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class EndClienteSerializer(serializers.ModelSerializer):
    permission_classes = (IsAuthenticated,)

    class Meta:
        model = Endereco
        fields = '__all__'


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'rua', 'bairro', 'numero', 'cep', 'cidade', 'uf']


class ClienteSerializer(serializers.ModelSerializer):
    permission_classes = (IsAuthenticated,)
    enderecos = EnderecoSerializer(many=True)

    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'sexo', 'telefone', 'celular', 'email', 'dtnasc', 'cpf', 'rg', 'enderecos']

    def create(self, validated_data):
        enderecos = validated_data.pop('enderecos')
        instance = Cliente.objects.create(**validated_data)
        instance.save()

        if enderecos is not None:
            for endereco in enderecos:
                Endereco.objects.create(idcliente=instance, **endereco)
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr is not 'enderecos':
                setattr(instance, attr, value)
        instance.save()
        return instance
