#BIBLIOTECAS
import warnings
'''from classes import *'''
import classes
import pyodbc
from datetime import datetime, date
import pandas as pd
from tabulate import tabulate
import os
import time


#LIMPA CONSOLE e SLEEP
def limpa():
    os.system('cls')
def delay(x):
    time.sleep(x)


#CONEXÃO COM O BANCO DE DADOS
def conexaoBD():
    server = ''
    driver = '{ODBC Driver 18 for SQL Server}'
    database = ''
    username = ''
    Authentication = 'ActiveDirectoryInteractive'
    port = '1433'
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';PORT='+port+';DATABASE='+database+';UID='+username)
    cursor = conn.cursor()
    return cursor
conex = conexaoBD()








#--------- GETS E SETS PARA CONSULTAS A INSERÇÃO DE DADOS ----------#
#CARTÕES
def get_cartao():
        server = ''
        driver = '{ODBC Driver 18 for SQL Server}'
        database = ''
        username = ''
        Authentication = 'ActiveDirectoryInteractive'
        port = '1433'
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';PORT='+port+';DATABASE='+database+';UID='+username)

        query = f"""SELECT * FROM [lucas_ferreira.cartao]"""
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            df = pd.read_sql(query, conn)
        tabela = df
        cabecalho = ['ID CARTAO', 'CREDITOS DISPONIVEIS', 'TIPO CARTAO', 'DATA DE EMISSÃO', 'ID USUARIO']
        print(tabulate(tabela, showindex="never", headers=cabecalho, tablefmt='psql'))
        
def criar_cartao(menu): 
    cartao = classes.Cartao
    cartao.data_emissao = date.today()
    cartao.creditos_disponiveis = "0"
    
    #VERIFICA QUAIS USUARIOS ESTÃO CADASTRADOS NA TABELA USUARIOS, CRIA UMA LISTA COM SEUS IDs
    lista_usuarios = []
    conex.execute(f"""SELECT id_usuario FROM [lucas_ferreira.usuario]""")
    records = conex.fetchall()
    for row in records:
        lista_usuarios.append(row[0])

    #VERIFICA QUAIS USUÁRIO ESTÃO CADASTRADOS NA TABELA CARTÕES, CRIA UMA LISTA COM SEUS IDs
    lista_cartoes = []
    conex.execute(f"""SELECT id_usuario FROM [lucas_ferreira.cartao]""")
    records2 = conex.fetchall()
    for row in records2:
        lista_cartoes.append(row[0])
    
    #IMPRIME QUAIS USUÁRIOS AINDA NÃO POSSUEM CARTÃO, SE TODOS TEM CARTAO PEDE PRA CRIAR NOVO USUARIO
    for identif in lista_usuarios:
        if identif not in lista_cartoes:
            print(f"USUÁRIOS SEM CARTÃO [IDs={identif}]")
            id_digitada = int(input("\n Para qual usuário será criado um novo cartão? [Digite o ID]: "))
        elif len(lista_usuarios) == len(lista_cartoes):
            print("TODOS OS USUÁRIOS JÁ POSSUEM CARTÕES ASSOCIADOS")
            print("Primeiro Cadastre um novo usuário \n")
            menu()
    
    
    #SÓ CRIA CARTÃO SE O USUÁRIO EXISTIR NA TABELA 'USUÁRIO' E NÃO TIVER NENHUM CARTAO'
    if (id_digitada in lista_usuarios) and (id_digitada not in lista_cartoes): 
            cartao.tipo_cartao = input("Qual o tipo do cartão? [normal, estudante, idoso]: ")
            conex.execute(f"""
            INSERT INTO [lucas_ferreira.cartao] (creditos_disponiveis, tipo_cartao, data_emissao, id_usuario)
            VALUES ('{cartao.creditos_disponiveis}','{cartao.tipo_cartao}','{cartao.data_emissao}','{id_digitada}')
            """)
            conex.commit()
            print("\n CARTÃO CADASTRADO COM SUCESSO!")  
    
    #SE O USUARIO EXISTE E JÁ TEM CARTÃO CADASTRADO, NAO PERMITE CRIAR MAIS UM
    elif (id_digitada in lista_usuarios) and (id_digitada in lista_cartoes): 
            print("\nEste usuário já possui um cartão associado")
            print("Tente novamente ...")
            criar_cartao(menu)
    
    #SE O USUÁRIO NAO EXISTE, NÃO PERMITE CRIAR CARTÃO
    elif id_digitada not in lista_usuarios: 
        print("\n ID INVÁLIDO! Usuário não cadastrado")
        print("Tente Novamente ...")
        criar_cartao(menu)

def deletar_cartao(conex, menu):
    conn = conex
    
    lista_usuarios = []
    conex.execute(f"""SELECT id_usuario FROM [lucas_ferreira.usuario]""")
    records = conex.fetchall()
    for row in records:
        lista_usuarios.append(row[0])

    id_delete = int(input("Qual o ID do usuário que deseja deletar o cartão? "))

    if id_delete in lista_usuarios:
        query = f"""DELETE FROM [lucas_ferreira.cartao] WHERE id_usuario = {id_delete}"""
        conn.execute(query)
        conn.commit()
        print("CARTÃO DELETADO COM SUCESSO!")
    
    elif id_delete not in lista_usuarios: 
        print("\n ID INVÁLIDO! Usuário não cadastrado")
        print("Tente Novamente ...")
        menu()
    
def inserir_credito():
    conex
 
    #SÓ PERMITIR INSERIR CRÉDITOS SE O CARTÃO EXISTIR
    lista_cartoes = []
    conex.execute(f"""SELECT id_usuario FROM [lucas_ferreira.cartao]""")
    records = conex.fetchall()
    for row in records:
        lista_cartoes.append(row[0])

    id_digitada = int(input('\n QUAL A ID DO USUÁRIO?: '))

    if id_digitada in lista_cartoes:
        credito_atual = conex.execute(f"""
        SELECT creditos_disponiveis FROM [lucas_ferreira.cartao] 
        WHERE id_usuario = {id_digitada}
        """)
        
        credito_atual2 = credito_atual.fetchone()[0]
        valor_inserir = int(input("Valor que deseja inserir para este usuário: "))
        valor_inserir2 = credito_atual2 + valor_inserir

        conex.execute(f"""
        UPDATE [lucas_ferreira.cartao] SET creditos_disponiveis = {valor_inserir2}
        WHERE id_usuario = {id_digitada}
        """)

        conex.commit()
        print(f"""\n FOI ADICIONADO +{valor_inserir} AO CARTÃO""")

    elif id_digitada not in lista_cartoes:
        print("Este cartão não existe, tente novamente")
        inserir_credito()



#USUARIOS
def get_usuario():
        server = ''
        driver = '{ODBC Driver 18 for SQL Server}'
        database = ''
        username = ''
        Authentication = 'ActiveDirectoryInteractive'
        port = '1433'
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';PORT='+port+';DATABASE='+database+';UID='+username)

        query = f"""SELECT * FROM [lucas_ferreira.usuario]"""
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            df = pd.read_sql(query, conn)
        tabela = df
        cabecalho = ['NOME', 'SOBRENOME', 'EMAIL', 'BAIRRO', 'DATA NASCIMENTO', 'ID USUARIO']
        print(tabulate(tabela, showindex="never", headers=cabecalho, tablefmt='psql'))

def criar_usuario(): 
    usuario = classes.Usuario
    usuario.nome_usuario = input("Digite o nome do usuário: ")
    usuario.sobrenome_usuario = input("Digite o sobrenome: ")
    usuario.email_usuario = input("Digite o email: ")
    usuario.bairro_usuario = input("Nome do bairro: ")
    usuario.nascimento_usuario = input("Data de nascimento [dd/mm/aaaa]: ")

    data_formatada = datetime.strptime(usuario.nascimento_usuario, '%d/%m/%Y').strftime('%Y-%m-%d')


    conex.execute(f"""
        INSERT INTO [lucas_ferreira.usuario] (nome_usuario, sobrenome_usuario, email_usuario, bairro_usuario, nascimento_usuario)
        VALUES ('{usuario.nome_usuario}','{usuario.sobrenome_usuario}','{usuario.email_usuario}','{usuario.bairro_usuario}','{data_formatada}')
        """)
    conex.commit()
    print("\n USUÁRIO CADASTRADO COM SUCESSO \n")

def deletar_usuario(conex, menu):
    conn = conex
    
    lista_usuarios = []
    conex.execute(f"""SELECT id_usuario FROM [lucas_ferreira.usuario]""")
    records = conex.fetchall()
    for row in records:
        lista_usuarios.append(row[0])

    id_delete = int(input("Qual o ID do usuário que deseja deletar? "))

    if id_delete in lista_usuarios:
        query = f"""DELETE FROM [lucas_ferreira.usuario] WHERE id_usuario = {id_delete}"""
        conn.execute(query)
        conn.commit()
        print("USUÁRIO DELETADO COM SUCESSO!")
    
    elif id_delete not in lista_usuarios: 
        print("\n ID INVÁLIDO! Usuário não cadastrado")
        print("Tente Novamente ...")
        menu()
    


#ONIBUS
def get_onibus():
        server = ''
        driver = '{ODBC Driver 18 for SQL Server}'
        database = ''
        username = ''
        Authentication = 'ActiveDirectoryInteractive'
        port = '1433'
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';PORT='+port+';DATABASE='+database+';UID='+username)

        query = f"""SELECT * FROM [lucas_ferreira.onibus]"""
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            df = pd.read_sql(query, conn)
        tabela = df
        cabecalho = ['PLACA', 'NUMERO LINHA', 'MODELO ÔNIBUS', 'ID MOTORISTA']
        print(tabulate(tabela, showindex="never", headers=cabecalho, tablefmt='psql'))

def criar_onibus(): 
    onibus = classes.Onibus
    onibus.numero_placa = input("Digite a placa do ônibus: ")
    onibus.numero_linha = input("Qual o número da linha deste ônibus?: ")
    onibus.modelo_onibus = input("Qual o modelo do ônibus?: ")
    #onibus.ano_onibus = input("Qual a data de fabricação? [dd/mm/aaaa]: ")
    onibus.id_motorista = input("Qual o id do motorista deste ônibus: ")
 
    #data_formatada = datetime.strptime(onibus.ano_onibus, '%d/%m/%Y').strftime('%Y-%m-%d')

    conex.execute(f"""
        INSERT INTO [lucas_ferreira.onibus] (numero_placa, numero_linha, modelo_onibus, id_motorista)
        VALUES ('{onibus.numero_placa}','{onibus.numero_linha}','{onibus.modelo_onibus}','{onibus.id_motorista}')
        """)
    conex.commit()
    print("\n ÔNIBUS CADASTRADO COM SUCESSO \n")

def deletar_onibus(conex, menu):
    conn = conex
    
    lista_onibus = []
    conex.execute(f"""SELECT numero_placa FROM [lucas_ferreira.onibus]""")
    records = conex.fetchall()
    for row in records:
        lista_onibus.append(row[0])

    id_delete = input("Qual a placa do ônibus que deseja deletar? ")

    if id_delete in lista_onibus:
        query = f"""DELETE FROM [lucas_ferreira.onibus] WHERE numero_placa = {id_delete}"""
        conn.execute(query)
        conn.commit()
        print("ÔNIBUS DELETADO COM SUCESSO!")
    
    elif id_delete not in lista_onibus: 
        print("\n PLACA INVÁLIDA! Ônibus não cadastrado")
        print("Tente Novamente ...")
        menu()
    
    
    
    '''id_delete = input("Qual a placa do ônibus que deseja deletar? ")
    query = f"""DELETE FROM [lucas_ferreira.onibus] WHERE numero_placa = '{id_delete}'"""
    conn.execute(query)
    conn.commit()
    print(f"O ÔNIBUS COM A PLACA {id_delete} FOI DELETADO COM SUCESSO!")
'''


#MOTORISTAS
def get_motorista():
        server = ''
        driver = '{ODBC Driver 18 for SQL Server}'
        database = ''
        username = ''
        Authentication = 'ActiveDirectoryInteractive'
        port = '1433'
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';PORT='+port+';DATABASE='+database+';UID='+username)

        query = f"""SELECT * FROM [lucas_ferreira.motorista]"""
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            df = pd.read_sql(query, conn)
        tabela = df
        cabecalho = ['NUMERO CNH', 'NOME MOTORISTA', 'SOBRENOME', 'DATA NASCIMENTO', 'ID MOTORISTA']
        print(tabulate(tabela, showindex="never", headers=cabecalho, tablefmt='psql'))

def criar_motorista(): 
    motorista = classes.Motorista
    motorista.numero_cnh = input("Digite o número da CNH: ")
    motorista.nome_motorista = input("Digite o nome do motorista: ")
    motorista.sobrenome_motorista = input("Digite o sobrenome do motorista: ")
    motorista.nascimento_motorista = input("Digite o nascimento do motorista [dd/mm/aaaa]: ")

 
    data_formatada = datetime.strptime(motorista.nascimento_motorista, '%d/%m/%Y').strftime('%Y-%m-%d')

    conex.execute(f"""
        INSERT INTO [lucas_ferreira.motorista] (numero_cnh, nome_motorista, sobrenome_motorista, nascimento_motorista)
        VALUES ('{motorista.numero_cnh}','{motorista.nome_motorista}','{motorista.sobrenome_motorista}','{data_formatada}')
        """)
    conex.commit()
    print("\n MOTORISTA CADASTRADO COM SUCESSO \n")

def deletar_motorista(conex, menu):
    conn = conex

    lista_motoristas = []
    conex.execute(f"""SELECT id_motorista FROM [lucas_ferreira.motorista]""")
    records = conex.fetchall()
    for row in records:
        lista_motoristas.append(row[0])

    id_delete = int(input("Qual o ID do motorista que deseja deletar? "))

    if id_delete in lista_motoristas:
        query = f"""DELETE FROM [lucas_ferreira.motorista] WHERE id_motorista = {id_delete}"""
        conn.execute(query)
        conn.commit()
        print("MOTORISTA DELETADO COM SUCESSO!")
    
    elif id_delete not in lista_motoristas: 
        print("\n ID INVÁLIDO! Motorista não cadastrado")
        print("Tente Novamente ...")
        menu()

    '''id_delete = input("Qual o ID do motorista a ser deletado? ")
    query = f"""DELETE FROM [lucas_ferreira.motorista] WHERE id_motorista = {id_delete}"""
    conn.execute(query)
    conn.commit()
    print("O MOTORISTA FOI DELETADO COM SUCESSO!")'''
