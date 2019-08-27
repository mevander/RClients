#RClients

#####Tecnologias utilizadas

**- Python 3.7.4**
**- Django 2.2**

O Projeto **RClients** é o BackEnd do projeto **CClients**, as definições de uso dos endpoints foram subdividos em suas devidas respostas, **GET**, **POST** e **DELETE**.

Abaixo seguirá o contrato de como as respostas em _JSON_ serão retornadas e como os _REQUEST_ deverão ser enviadas a aplicação 

####EndPoints GET

**Obter lista de Clientes**

- <https://localhost:0000/Clientes/obterClientes>

**Response status**

- **200 OK** - Sucesso

**Json**

```json
[
    {
        "id": 0,
        "nome": "string",
        "endereco": "string",
        "cep": "string",
        "cidade": "string",
        "uf": "string",
        "telefone": "string",
        "celular": "string",
        "email": "string",
        "sexo": "string"
    },
    {
        "id": 1,
        "nome": "string",
        "endereco": "string",
        "cep": "string",
        "cidade": "string",
        "uf": "string",
        "telefone": "string",
        "celular": "string",
        "email": "string",
        "sexo": "string"
    }
    
]
````


**Obter Cliente Único**
- <https://localhost:0000/Clientes/obterCliente/{id}>

**Parâmetros**

- **ID** -  Id do cliente a ser retornado

**Response status**

- **200 OK** - Sucesso
- **404 Not Found** - Erro Id inexistente

**Json**

```json
[
    {
        "id": 0,
        "nome": "string",
        "endereco": "string",
        "cep": "string",
        "cidade": "string",
        "uf": "string",
        "telefone": "string",
        "celular": "string",
        "email": "string",
        "sexo": "string"
    }
]
````

