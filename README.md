📑 Sistema de Gerenciamento Clínico (CLI)
Este é um sistema desenvolvido em Python integrado com o banco de dados MySQL para gerenciar os cadastros, consultas e faturamento de uma clínica ou hospital. O sistema roda direto no terminal (linha de comando) com um menu numérico interativo e limpo.

🛠️ Tecnologias Utilizadas
Estruturação de Banco de Dados: Br Modelo

Linguagem da Programação: Python

Banco de Dados: MySQL

Conector: mysql-connector-python

Ambiente recomendado: Windows/Linux/macOS

📌 Funcionalidades Atuais
O sistema conta com um menu principal de 11 opções, divididas em quatro pilares principais (CRUD):

Cadastros (Create): Pacientes, Médicos e Consultas vinculadas a Faturas (usando transações seguras para não gerar faturamento sem consulta).

Pesquisas (Read): Filtros inteligentes para buscar pacientes (por nome/CPF), médicos (por nome/CRM), consultas e faturas.

Atualizações (Update): Alteração de dados cadastrais de pacientes e médicos sem apagar o que já existia.

Exclusões (Delete): Remoção de médicos e pacientes do sistema com tela de confirmação de segurança.

⚙️ Como Configurar o Banco de Dados
Antes de rodar o código Python, você precisa criar o banco de dados no seu MySQL (pode usar o MySQL Workbench).

Abra o seu cliente MySQL.

Copie e cole o script SQL que está no arquivo database.sql (ou use a estrutura das tabelas fornecidas).

Certifique-se de criar as tabelas de suporte (tb_hospital, tb_convenio, tb_especialidade) antes das tabelas principais para não dar erro de Chave Estrangeira (Foreign Key).

🚀 Como Rodar o Projeto
Certifique-se de ter o Python instalado na sua máquina.

Instale o conector do MySQL no seu terminal:

Bash
pip install mysql-connector-python

Abra o arquivo Python e ajuste as credenciais de conexão se o seu MySQL tiver senha:

Python
user="root",
passwd="SUA_SENHA_AQUI",
database="O_BANCO_DE_DADOS_VAI_AQUI" (CASO QUEIRA DEIXAR O BANCO DE DADOS PRÉ ATIVADO, PORÉM, PRECISA DELE CRIADO)
Execute o programa:

Bash
python nome_do_arquivo_código_do_software.py

🚧 Status do Projeto (Melhorias Futuras)
O projeto está na Fase 1 (Versão CLI). De acordo com o nosso planejamento ágil, as próximas implementações serão:

[ ] Validação de Inputs: Impedir que o sistema trave se o usuário digitar uma data ou CPF no formato errado.

[ ] Correção de Chaves Estrangeiras: Adicionar os campos de Hospital, Especialidade e Convênio na hora de cadastrar médicos e pacientes pelo Python.

[ ] Interface Gráfica: Mudar o sistema do terminal para uma janela bonitona com botões.

👥 Desenvolvedores
Michael Alves / Leonardo Fagundes, Vitor Hugo, Luidy

GitHub: https://github.com/MaikonWatterson/Software-Triaxon.git