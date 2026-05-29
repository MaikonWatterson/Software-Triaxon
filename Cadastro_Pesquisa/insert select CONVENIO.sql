USE cadastro_pesquisa;

INSERT INTO tb_convenio (conv_nome, conv_cnpj, conv_telefone, conv_plano) 
VALUES ('Unimed Nacional', '45.789.012/0001-55', '(31) 98877-6655', 'Unimed Alfa Coletivo'),
	   ('Amil Saúde', '29.309.123/0001-10', '(11) 98765-4321', 'Amil Fácil S60'),
       ('SulAmérica', '38.145.987/0001-22', '(21) 99988-7766', 'SulAmérica Exato');
       
SELECT * FROM tb_convenio;