CREATE TABLE Cliente (
    id int NOT NULL,
    nome varchar(100) NOT NULL,
    sexo varchar(15),
    telefone varchar(10),
    celular varchar(11),
    email varchar(50),
    dtNasc date,
    cpf varchar(11),
	rg varchar(9),
    PRIMARY KEY (id)
);

CREATE TABLE Endereco (
	id int NOT NULL,
	rua varchar(80),
    bairro varchar(80),
    numero varchar(10),
	cep varchar(8),
    cidade varchar(50),
    uf varchar(2),
    idcliente int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (idcliente) REFERENCES Cliente(id)
);

CREATE TABLE Usuario (
	id int NOT NULL,
	login varchar(30) NOT NULL,
    senha varchar(255) NOT NULL,
    PRIMARY KEY (id)
);