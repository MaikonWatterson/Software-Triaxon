USE cadastro_pesquisa;

INSERT INTO tb_especialidade (esp_nome, esp_descricao) VALUES 
('Cardiologia', 'Especialidade que cuida da saúde do coração e do sistema circulatório.'),
('Pediatria', 'Assistência médica dedicada a crianças e adolescentes.'),
('Dermatologia', 'Diagnóstico e tratamento de doenças da pele, cabelos e unhas.'),
('Ortopedia', 'Cuidado com o sistema locomotor, ossos, músculos e articulações.'),
('Neurologia', 'Especialidade focada em distúrbios do sistema nervoso central e periférico.');

SELECT * FROM tb_especialidade;