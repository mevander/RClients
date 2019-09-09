#RClients

#####Tecnologias utilizadas

**- Python 3.7.4**
**- Django 2.2**
**- Django Rest Framework**

O Projeto **RClients** é o BackEnd do projeto **CClients**, as definições de uso dos endpoints seguem o formato das aplicações padrões desenvolvidas com o Django Rest Framework, ou seja, um end-point trata de uma tabela que é representada por uma model, os verbos utilizados serão os **GET**, **POST**, **PUT** e **DELETE**.

Abaixo seguirá o contrato de como as respostas em _JSON_ serão retornadas e como os _REQUEST_ deverão ser enviadas a aplicação sendo que para os verbos **PUT** e **DELETE** as requisições deverão ser enviadas juntamente o parâmetro ID na URL. Os EndPoints serão dividos por sua Tabela(Model).

**Listar/Criar Clientes**

- <https://localhost:0000/Cliente/>

**Json**

```json
[
    {
        "id": 0,
        "nome": "String",
        "sexo": "String",
        "telefone": "String",
        "celular": "String",
        "email": "String",
        "dtnasc": "String",
        "cpf": "String",
        "rg": "String",
        "enderecos": [
            {
                "rua": "String",
                "bairro": "String",
                "numero": "String",
                "cep": "String",
                "cidade": "String",
                "uf": "String"
            }
        ]
    }
]
````


**Obter/Excluir/Atualizar Cliente**
- <https://localhost:0000/Cliente/{id}>

**Parâmetros**

- **ID** -  Id do cliente a ser retornado

**Json**

```json
{
    "id": 0,
    "nome": "String",
    "sexo": "String",
    "telefone": "String",
    "celular": "String",
    "email": "String",
    "dtnasc": "String",
    "cpf": "String",
    "rg": "String",
    "enderecos": [
        {
            "rua": "String",
            "bairro": "String",
            "numero": "String",
            "cep": "String",
            "cidade": "String",
            "uf": "String"
        }
    ]
}
````

**Criar/Listar Endereços**

- <https://localhost:0000/Endereco/>

**Response status**

- **200 OK** - Sucesso

**Json**

```json
[
    {
        "id": 0,
        "rua": "String",
        "bairro": "String",
        "numero": "String",
        "cep": "String",
        "cidade": "String",
        "uf": "String",
        "idcliente": 0
    }
]
````

**Obter/Excluir/Atualizar Endereco**
- <https://localhost:0000/Endereco/{id}>

**Parâmetros**

- **ID** -  Id do Endereco a ser retornado

**Json**

```json
    {
        "id": 0,
        "rua": "String",
        "bairro": "String",
        "numero": "String",
        "cep": "String",
        "cidade": "String",
        "uf": "String",
        "idcliente": 0
    }
````

