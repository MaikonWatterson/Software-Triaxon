USE cadastro_pesquisa;

INSERT INTO tb_hospital (hosp_nome, hosp_cnpj, hosp_telefone1, hosp_telefone2, hosp_endereco, hosp_numero, hosp_cep, hosp_bairro, hosp_cidade, hosp_estado)
VALUES ('Hospital Santa Helena', '12345678000199', '(11) 4002-8922', '(11) 4002-8923', 'Avenida das Nações', '4500', '04578-000', 'Brooklin', 'São Paulo', 'SP');

SELECT * FROM tb_hospital;