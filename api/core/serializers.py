from rest_framework import serializers
from .models import Cliente, Endereco


class EndClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'rua', 'bairro', 'numero', 'cep', 'cidade', 'uf']


class ClienteSerializer(serializers.ModelSerializer):
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
