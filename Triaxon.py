import os
import mysql.connector
from mysql.connector import Error

# Função para limpar a tela de forma multiplataforma (Windows, Linux, macOS)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para gerar conexões limpas com o banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="cadastro_pesquisa"
    )

# --- CADASTROS ---

def cadastrar_paciente():
    limpar_tela()
    print("=== CADASTRO DE PACIENTE ===")
    try:
        pac_nome = input("Nome: ").strip()
        pac_sobrenome = input("Sobrenome: ").strip()
        pac_cpf = input("CPF: ").strip()
        pac_data_nasc = input("Data de Nascimento (AAAA-MM-DD): ").strip()
        pac_telefone = input("Telefone: ").strip()
        pac_email = input("E-mail: ").strip()
        pac_endereco = input("Endereço: ").strip()
        pac_numero = input("Número: ").strip()
        pac_cep = input("CEP: ").strip()
        pac_bairro = input("Bairro: ").strip()
        pac_cidade = input("Cidade: ").strip()
        pac_estado = input("Estado (UF): ").strip()

        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO tb_paciente (
                pac_nome, pac_sobrenome, pac_cpf, pac_data_nasc, 
                pac_telefone, pac_email, pac_endereco, pac_numero, 
                pac_cep, pac_bairro, pac_cidade, pac_estado
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (pac_nome, pac_sobrenome, pac_cpf, pac_data_nasc, pac_telefone, pac_email, pac_endereco, pac_numero, pac_cep, pac_bairro, pac_cidade, pac_estado)
        cursor.execute(sql, valores)
        conn.commit()
        
        print("\nPaciente cadastrado com sucesso!")
        cursor.close()
        conn.close()
        
    except Error as e:
        print(f"\nErro MySQL: {e}")
    except Exception as e:
        print(f"\nErro geral: {e}")


def cadastrar_medico():
    limpar_tela()
    print("=== CADASTRO DE MÉDICO ===")
    try:
        med_nome = input("Nome: ").strip()
        med_sobrenome = input("Sobrenome: ").strip()
        crm = input("CRM: ").strip()
        med_cpf = input("CPF: ").strip()        
        med_telefone = input("Telefone: ").strip()
        med_email = input("E-mail: ").strip()
        med_data_admissao = input("Data de Admissão (AAAA-MM-DD): ").strip()
        med_data_demissao = input("Data de Demissão (Pressione Enter se ativo): ").strip()
        med_data_demissao = med_data_demissao if med_data_demissao else None
        med_endereco = input("Endereço: ").strip()
        med_numero = input("Número: ").strip()
        med_cep = input("CEP: ").strip()
        med_bairro = input("Bairro: ").strip()
        med_cidade = input("Cidade: ").strip()
        med_estado = input("Estado (UF): ").strip()

        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO tb_medico (
                med_nome, med_sobrenome, crm, med_cpf, med_telefone, 
                med_email, med_data_admissao, med_data_demissao, med_endereco, 
                med_numero, med_cep, med_bairro, med_cidade, med_estado
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (med_nome, med_sobrenome, crm, med_cpf, med_telefone, med_email, med_data_admissao, med_data_demissao, med_endereco, med_numero, med_cep, med_bairro, med_cidade, med_estado)
        cursor.execute(sql, valores)
        conn.commit()
        
        print("\nMédico cadastrado com sucesso!")
        cursor.close()
        conn.close()    
        
    except Error as e:
        print(f"\nErro MySQL: {e}")
    except Exception as e:
        print(f"\nErro geral: {e}")


# --- PESQUISAS ---

def pesquisar_paciente():
    limpar_tela()
    print("=== PESQUISAR PACIENTE ===")
    print("Preencha um ou ambos os campos (ou deixe em branco para ver todos):")
    nome = input("Nome (ou parte dele): ").strip()
    cpf = input("CPF: ").strip()

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True) # Adicionado dictionary=True para mapear as chaves corretamente

        sql = "SELECT * FROM tb_paciente WHERE 1=1"
        valores_lista = []
        
        if nome:
            sql += " AND pac_nome LIKE %s"
            valores_lista.append(f"%{nome}%")
        if cpf:
            sql += " AND pac_cpf = %s"
            valores_lista.append(cpf)
            
        cursor.execute(sql, tuple(valores_lista))
        resultados = cursor.fetchall()

        if resultados:
            print(f"\nResultados encontrados ({len(resultados)}):")
            print("-" * 120)
            for r in resultados:
                print(f"ID: {r['pac_id']} | Nome: {r['pac_nome']} {r['pac_sobrenome']} | CPF: {r['pac_cpf']} | Telefone: {r['pac_telefone']} | Email: {r['pac_email']}")
            print("-" * 120)
        else:
            print("\nNenhum paciente encontrado com esses critérios.")

        cursor.close()
        conn.close()

    except Error as e:
        print(f"\nErro ao pesquisar paciente: {e}")


def pesquisar_medico():
    limpar_tela()
    print("=== PESQUISAR MÉDICO ===")
    print("Preencha um ou ambos os campos (ou deixe em branco para ver todos):")
    med_nome = input("Nome (ou parte dele): ").strip()
    crm = input("CRM: ").strip()

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        sql = "SELECT * FROM tb_medico WHERE 1=1"
        valores_lista = []
        
        if med_nome:
            sql += " AND med_nome LIKE %s"
            valores_lista.append(f"%{med_nome}%")
        if crm:
            sql += " AND crm = %s"
            valores_lista.append(crm)
      
        cursor.execute(sql, tuple(valores_lista))
        resultados = cursor.fetchall()

        if resultados:
            print(f"\nResultados encontrados ({len(resultados)}):")
            print("-" * 60)
            for r in resultados:
                print(f"ID: {r['med_id']} | Nome: {r['med_nome']} {r['med_sobrenome']} | CRM: {r['crm']}")
            print("-" * 60)
        else:
            print("\nNenhum médico encontrado com esses critérios.")

        cursor.close()
        conn.close()

    except Error as e:
        print(f"\nErro ao pesquisar médico: {e}")


# --- ATUALIZAÇÕES (UPDATE) ---

def atualizar_paciente():
    limpar_tela()
    print("=== ATUALIZAR PACIENTE ===")
    try:
        pac_id = input("Digite o ID do paciente que deseja alterar: ").strip()
        print("\nDeixe em branco os campos que NÃO deseja alterar:")
        novo_nome = input("Novo Nome: ").strip()
        novo_sobrenome = input("Novo Sobrenome ").strip()
        novo_telefone = input("Novo Telefone: ").strip()
        novo_email = input("Novo E-mail: ").strip()

        # Montagem dinâmica do UPDATE para alterar apenas o que foi digitado
        campos = []
        valores = []

        if novo_nome:
            campos.append("pac_nome = %s")
            valores.append(novo_nome)
        if novo_sobrenome:
            campos.append("pac_sobrenome = %s")
            valores.append(novo_sobrenome)
        if novo_telefone:
            campos.append("pac_telefone = %s")
            valores.append(novo_telefone)
        if novo_email:
            campos.append("pac_email = %s")
            valores.append(novo_email)

        if not campos:
            print("\nNenhuma alteração foi digitada.")
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Junta os campos alterados separados por vírgula
        sql = f"UPDATE tb_paciente SET {', '.join(campos)} WHERE pac_id = %s"
        valores.append(pac_id) # Adiciona o ID para a cláusula WHERE

        cursor.execute(sql, tuple(valores))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"\nPaciente ID {pac_id} atualizado com sucesso!")
        else:
            print("\nNenhum registro foi alterado (verifique se o ID existe).")

        cursor.close()
        conn.close()

    except Error as e:
        print(f"\nErro MySQL: {e}")


def atualizar_medico():
    limpar_tela()
    print("=== ATUALIZAR MÉDICO ===")
    try:
        med_id = input("Digite o ID do médico que deseja alterar: ").strip()
        print("\nDeixe em branco os campos que NÃO deseja alterar:")
        novo_nome = input("Novo Nome: ").strip()
        novo_crm = input("Novo CRM: ").strip()
        nova_data_demissao = input("Data de Demissão (AAAA-MM-DD): ").strip()

        campos = []
        valores = []

        if novo_nome:
            campos.append("med_nome = %s")
            valores.append(novo_nome)
        if novo_crm:
            campos.append("crm = %s")
            valores.append(novo_crm)
        if nova_data_demissao:
            campos.append("med_data_demissao = %s")
            valores.append(nova_data_demissao)

        if not campos:
            print("\nNenhuma alteração foi digitada.")
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = f"UPDATE tb_medico SET {', '.join(campos)} WHERE med_id = %s"
        valores.append(med_id)

        cursor.execute(sql, tuple(valores))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"\nMédico ID {med_id} atualizado com sucesso!")
        else:
            print("\nNenhum registro foi alterado (verifique se o ID existe).")

        cursor.close()
        conn.close()

    except Error as e:
        print(f"\nErro MySQL: {e}")


# --- EXCLUSÕES (DELETE) ---

def deletar_paciente():
    limpar_tela()
    print("=== DELETAR PACIENTE ===")
    try:
        pac_id = input("Digite o ID do paciente que deseja EXCLUIR: ").strip()
        
        # Confirmação de segurança antes de apagar
        confirmar = input(f"Tem certeza que deseja apagar o paciente ID {pac_id}? (S/N): ").strip().upper()
        if confirmar != 'S':
            print("\nOperação cancelada.")
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Sintaxe correta do DELETE
        sql = "DELETE FROM tb_paciente WHERE pac_id = %s"
        
        cursor.execute(sql, (pac_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print("\nPaciente excluído com sucesso!")
        else:
            print("\nNenhum paciente encontrado com este ID.")
            
        cursor.close()
        conn.close()
        
    except Error as e:
        print(f"\nErro MySQL: {e}")


def deletar_medico():
    limpar_tela()
    print("=== DELETAR MÉDICO ===")
    try:
        med_id = input("Digite o ID do médico que deseja EXCLUIR: ").strip()
        
        confirmar = input(f"Tem certeza que deseja apagar o médico ID {med_id}? (S/N): ").strip().upper()
        if confirmar != 'S':
            print("\nOperação cancelada.")
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = "DELETE FROM tb_medico WHERE med_id = %s"
        
        cursor.execute(sql, (med_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print("\nMédico excluído com sucesso!")
        else:
            print("\nNenhum médico encontrado com este ID.")
            
        cursor.close()
        conn.close()
        
    except Error as e:
        print(f"\nErro MySQL: {e}")


# --- MENU PRINCIPAL ---

def menu():
    while True:
        limpar_tela()
        print("\n┌────────────────────────────────────────┐")
        print("│        SISTEMA DE GERENCIAMENTO        │")
        print("├────────────────────────────────────────┤")
        print("│  [ 1 ] Cadastrar Novo Paciente         │")
        print("│  [ 2 ] Cadastrar Novo Médico           │")
        print("│  [ 3 ] Pesquisar Paciente              │")
        print("│  [ 4 ] Pesquisar Médico                │")
        print("│  [ 5 ] Atualizar Paciente              │")
        print("│  [ 6 ] Atualizar Médico                │")
        print("│  [ 7 ] Deletar Paciente                │")
        print("│  [ 8 ] Deletar Médico                  │")
        print("│                                        │")
        print("│  [ 0 ] Sair do Programa                │")
        print("└────────────────────────────────────────┘")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_paciente()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "2":
            cadastrar_medico()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "3":
            pesquisar_paciente()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "4":
            pesquisar_medico()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "5":
            atualizar_paciente()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "6":
            atualizar_medico()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "7":
            deletar_paciente()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "8":
            deletar_medico()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "0":
            print("\nEncerrando o sistema... Até logo!")
            break
        else:
            print("\nOpção inválida! Digite um número de 0 a 8.")
            input("Pressione Enter para tentar novamente...")

if __name__ == '__main__':
    menu()