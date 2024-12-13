CREATE TABLE contatos(
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(15),
    cep VARCHAR(10)
);