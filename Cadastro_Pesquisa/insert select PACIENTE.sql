USE cadastro_pesquisa;

INSERT INTO tb_paciente (pac_nome, pac_sobrenome, pac_cpf, pac_data_nasc, pac_telefone, pac_email, pac_endereco, pac_numero, pac_cep, pac_bairro, pac_cidade, pac_estado, pac_hospid, pac_convid)
VALUES ('Lucas', 'Oliveira Santos', '111.222.333-44', '1995-03-15', '(11) 97777-8888', 'lucas.oliveira@email.com', 'Rua das Flores', '123', '04123-000', 'Saúde', 'São Paulo', 'SP', 1, 1),
	   ('Beatriz', 'Almeida Lima', '222.333.444-55', '1988-11-22', '(21) 96666-5555', 'beatriz.lima@email.com', 'Av. Atlântica', '850', '22070-000', 'Copacabana', 'Rio de Janeiro', 'RJ', 1, 2),
	   ('Thiago', 'Pereira Souza', '333.444.554-66', '2001-07-05', '(31) 95555-4444', 'thiago.souza@email.com', 'Rua Bahia', '45', '30160-010', 'Centro', 'Belo Horizonte', 'MG', 1, 3),
	   ('Larissa', 'Rocha Mendes', '444.555.666-77', '1975-12-30', '(41) 94444-3333', 'larissa.mendes@email.com', 'Alameida Júlia', '1012', '80420-000', 'Batel', 'Curitiba', 'PR', 1, 1),
	   ('Bruno', 'Ferreira Costa', '555.666.777-88', '1992-05-18', '(85) 93333-2222', 'bruno.costa@email.com', 'Rua Tibúrcio Cavalcante', '300', '60125-100', 'Aldeota', 'Fortaleza', 'CE', 1, 2);

SELECT * FROM tb_paciente;