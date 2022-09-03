#BIBLIOTECAS
#from codecs import charmap_build
#from colorama import Fore, Back, Style
from datetime import date
import random
import pyodbc
from dataclasses import dataclass
import os
os.system('cls')


#CONEXÃO COM O BANCO DE DADOS
server = ''
driver = '{ODBC Driver 18 for SQL Server}'
database = ''
username = ''
Authentication = 'ActiveDirectoryInteractive'
port = '1433'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';PORT='+port+';DATABASE='+database+';UID='+username)
cursor = conn.cursor()


# CRIAÇÃO DAS CLASSES
class Usuario:
    nome_usuario: str
    sobrenome_usuario: str
    email_usuario: str
    bairro_usuario: str
    nascimento_usuario: str
    id_usuario: int 

@dataclass
class Cartao:
    id_cartao: str = ''
    creditos_disponiveis: str =''
    tipo_cartao: str = ''
    data_emissao: str = ''
    id_usuario: str = ''


    def get_cartao(self, cursor):
        cursor.execute(f"""
        SELECT (id_cartao, creditos_disponiveis, tipo_cartao, data_emissao, id_usuario) 
        FROM [lucas_ferreira.cartao]
        WHERE id_cartao LIKE {'id_digitado'}
        """)
        return self.id_cartao, self.creditos_disponiveis, self.tipo_cartao, self.data_emissao, self.id_usuario
    

    def set_cartao(self, cursor):
        cursor.execute(f"""
        INSERT INTO [lucas_ferreira.cartao] (id_cartao, creditos_disponiveis, tipo_cartao, data_emissao, id_usuario)
        VALUES ('{self.id_cartao}','{self.creditos_disponiveis}','{self.tipo_cartao}','{self.data_emissao}','{self.id_usuario}')
        """)
    

class Onibus:
    numero_placa: int
    numero_linha: int
    modelo_onibus: str
    ano_onibus: str
    id_motorista: int

class Motorista:
    numero_cnh: int
    nome_motorista: str
    sobrenome_motorista: str
    nascimento_motorista: str
    id_motorista: int



#MENUS
def menu_principal():
    print('[1] REALIZAR CADASTROS')
    print('[2] CONSULTAS')
    print('[3] INSERIR CRÉDITO')
    print('[4] DELETAR DADOS')
    print('[5] SAIR')
    opcao_usuario = input('\n ESCOLHA A OPÇÃO DESEJADA: ')
    if opcao_usuario == "1":
        menu_cadastros()
    elif opcao_usuario == "2":
        menu_consultas()
    elif opcao_usuario == "3":
        menu_inserir_credito()
    elif opcao_usuario == "4":
        menu_deletar()
    elif opcao_usuario == "5":
        print('Obrigado, Volte Sempre!')
        quit()
    else:
        print('Opção inválida, tente novamente!')
        menu_principal()

def menu_cadastros():
    print('[1] CADASTRAR USUÁRIO')
    print('[2] CADASTRAR MOTORISTA') 
    print('[3] CADASTRAR CARTÃO')
    print('[4] CADASTRAR ÔNIBUS')
    print('[5] MENU PRINCIPAL')
    opcao_usuario2 = input('\n ESCOLHA A OPÇÃO DESEJADA:')
    if opcao_usuario2 == "1":
        print('x')
    elif opcao_usuario2 == "2":
        print('x')
    elif opcao_usuario2 == "3":
        #função criar cartao ... 
        tipo_cartao = input("Digite qual será o tipo do cartão: ")
        id_cartao = "1"
        data_emissao = date.today()
        id_usuario = "1"
        creditos_disponiveis = "0.0"
        cartaoX = Cartao(id_cartao, creditos_disponiveis, tipo_cartao, data_emissao, id_usuario)
        Cartao.set_cartao(cartaoX, cursor)
    elif opcao_usuario2 == "4":
        print('x')
    elif opcao_usuario2 == "5":
        menu_principal()
    else:
        print('Opção inválida, tente novamente!')
        menu_cadastros()

def menu_consultas():
    print('[1] VISUALIZAR USUÁRIO')
    print('[2] VISUALIZAR MOTORISTAS')
    print('[3] VISUALIZAR CARTÕES E SALDO')
    print('[4] VISUALIZAR FROTA DE ÔNIBUS')
    print('[5] MENU PRINCIPAL')
    opcao_usuario2 = input('\n ESCOLHA A OPÇÃO DESEJADA:')
    if opcao_usuario2 == "1":
        print('x')
    elif opcao_usuario2 == "2":
        print('x')
    elif opcao_usuario2 == "3":
        print('x')
    elif opcao_usuario2 == "4":
        print('x')
    elif opcao_usuario2 == "5":
        menu_principal()
    else:
        print('Opção inválida, tente novamente!')
        menu_consultas()

def menu_inserir_credito():
    print('[1] COMUM')
    print('[2] ESTUDANTE')
    print('[3] VALE-TRANSPORTE')
    print('[4] IDOSO')
    print('[5] MENU PRINCIPAL')
    opcao_usuario2 = input('\n QUAL O TIPO DO SEU CARTÃO?: ')
    if opcao_usuario2 == "1":
        print('x')
    elif opcao_usuario2 == "2":
        print('x')
    elif opcao_usuario2 == "3":
        print('x')
    elif opcao_usuario2 == "4":
        print('x')
    elif opcao_usuario2 == "5":
        menu_principal()
    else:
        print('Opção inválida, tente novamente!')
        menu_consultas()

def menu_deletar():
    print('[1] DELETAR USUÁRIO')
    print('[2] DELETAR MOTORISTA')
    print('[3] DELETAR CARTÃO')
    print('[4] MENU PRINCIPAL')
    opcao_usuario2 = input('\n ESCOLHA A OPÇÃO DESEJADA:')
    if opcao_usuario2 == "1":
        print('x')
    elif opcao_usuario2 == "2":
        print('x')
    elif opcao_usuario2 == "3":
        print('x')
    elif opcao_usuario2 == "4":
        menu_principal()
    else:
        print('Opção inválida, tente novamente!')
        menu_consultas()


menu_principal()