CREATE DATABASE cadastro_pesquisa;

USE cadastro_pesquisa;

DROP DATABASE cadastro_pesquisa;

CREATE TABLE tb_hospital(
	hosp_id INT AUTO_INCREMENT PRIMARY KEY,
    hosp_nome VARCHAR(150) NOT NULL,
	hosp_sobrenome VARCHAR(150) NOT NULL,
    hosp_cnpj VARCHAR(14) UNIQUE NOT NULL,
    hosp_telefone1 VARCHAR(15) NOT NULL,
    hosp_telefone2 VARCHAR(15),
    hosp_telefone3 VARCHAR(15),
    data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP,
    hosp_rua VARCHAR(150) NOT NULL,
    hosp_numero VARCHAR(150) NOT NULL,
    hosp_cep VARCHAR(10) NOT NULL,
    hosp_bairro VARCHAR(150),
    hosp_cidade VARCHAR(150)
);

DESCRIBE tb_medico;

CREATE TABLE tb_medico (
	med_id INT AUTO_INCREMENT PRIMARY KEY,
    med_nome VARCHAR(150) NOT NULL,
    med_sobrenome VARCHAR(150) NOT NULL,
    crm VARCHAR(14) UNIQUE NOT NULL,
    med_cpf VARCHAR(14) NOT NULL,
    med_telefone VARCHAR(14) NOT NULL,
    med_email VARCHAR(150) UNIQUE NOT NULL,
    med_data_admissao DATETIME DEFAULT CURRENT_TIMESTAMP,
    med_data_demissao DATETIME DEFAULT CURRENT_TIMESTAMP,
    med_endereco VARCHAR(150) NOT NULL,
    med_numero VARCHAR(5) NOT NULL,
    med_cep VARCHAR(9) NOT NULL,
    med_bairro VARCHAR(150),
    med_cidade VARCHAR(150),
    med_estado CHAR(2),
    med_hospid INT,
    med_espid INT,
    FOREIGN KEY (med_hospid) REFERENCES tb_hospital(hosp_id),
    FOREIGN KEY (med_espid) REFERENCES tb_especialidade(esp_id)
);

CREATE TABLE tb_especialidade (
	esp_id INT AUTO_INCREMENT PRIMARY KEY,
    esp_nome VARCHAR(150) NOT NULL,
    esp_descricao VARCHAR(255)
);

CREATE TABLE tb_consulta (
	cons_id INT AUTO_INCREMENT PRIMARY KEY,
    cons_diagnostico VARCHAR(150),
    cons_motivo VARCHAR(150),
    cons_datahora TIMESTAMP NOT NULL,
    cons_pacid INT,
    cons_medid INT,
    FOREIGN KEY (cons_pacid) REFERENCES tb_paciente(pac_id),
    FOREIGN KEY (cons_medid) REFERENCES tb_medico(med_id)
);

CREATE TABLE tb_paciente (
	pac_id INT AUTO_INCREMENT PRIMARY KEY,
    pac_nome VARCHAR(150) NOT NULL,
    pac_sobrenome VARCHAR(150) NOT NULL,
    pac_cpf VARCHAR(14) UNIQUE NOT NULL,
    pac_data_nasc DATE NOT NULL,
    pac_telefone VARCHAR(14) NOT NULL,
    pac_email VARCHAR(150) UNIQUE NOT NULL,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    pac_endereco VARCHAR(150) NOT NULL,
    pac_numero VARCHAR(5) NOT NULL,
    pac_cep VARCHAR(9) NOT NULL,
    pac_bairro VARCHAR(150),
    pac_cidade VARCHAR(150),
    pac_estado CHAR(2),
    pac_hospid INT,
    pac_convid INT,
    FOREIGN KEY (pac_hospid) REFERENCES tb_hospital(hosp_id),
    FOREIGN KEY (pac_convid) REFERENCES tb_convenio(conv_id)
    );
    
    CREATE TABLE tb_convenio (
	conv_id INT AUTO_INCREMENT PRIMARY KEY,
    conv_nome VARCHAR(255) NOT NULL,
    conv_cnpj VARCHAR(18) UNIQUE NOT NULL,
    conv_telefone VARCHAR(15) NOT NULL,
    conv_plano VARCHAR(255) NOT NULL
);

SELECT * FROM tb_paciente;