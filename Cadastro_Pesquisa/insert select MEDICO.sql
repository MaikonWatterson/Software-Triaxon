USE cadastro_pesquisa;

INSERT INTO tb_medico (med_nome, med_sobrenome, crm, med_cpf, med_telefone, med_email, med_endereco, med_numero, med_cep, med_bairro, med_cidade, med_estado, med_hospid, med_espid)
VALUES ('Carlos', 'Eduardo Silva', 'CRM/SP 123456', '123.456.789-00', '(11) 91234-5678', 'carlos.silva@email.com', 'Av. Paulista', '1000', '01311-100', 'Bela Vista', 'São Paulo', 'SP', 1, 1),
	   ('Ana', 'Beatriz Souza', 'CRM/RJ 654321', '234.567.890-11', '(21) 98765-4321', 'ana.souza@email.com', 'Rua Copacabana', '450', '22020-002', 'Copacabana', 'Rio de Janeiro', 'RJ', 1, 2),
	   ('Mariana', 'Costa Ribeiro', 'CRM/MG 789123', '345.678.901-22', '(31) 99887-7665', 'mariana.costa@email.com', 'Av. Afonso Pena', '2500', '30130-009', 'Funcionários', 'Belo Horizonte', 'MG', 1, 3),
	   ('Ricardo', 'Almeida Santos', 'CRM/PR 321987', '456.789.012-33', '(41) 99112-2334', 'ricardo.santos@email.com', 'Rua XV de Novembro', '120', '80020-310', 'Centro', 'Curitiba', 'PR', 1, 4),
	   ('Juliana', 'Mendes Frota', 'CRM/CE', '567.890.123-44', '(85) 98888-7777', 'juliana.mendes@email.com', 'Av. Beira Mar', '3500', '60165-121', 'Meireles', 'Fortaleza', 'CE', 1, 5);

SELECT * FROM tb_medico;