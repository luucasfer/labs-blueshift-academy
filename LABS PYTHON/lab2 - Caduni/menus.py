#BIBLIOTECAS
from colorama import Fore, Back, Style
from funcoes import *


#MENUS
def menu_principal():
    print("\n")
    print(" ---- MENU PRINCIPAL ----")
    print('[1] CADASTRAR')
    print('[2] CONSULTAR')
    print('[3] INSERIR CRÉDITO')
    print('[4] DELETAR')
    print('[5] SAIR')
    opcao_usuario = input('\n ESCOLHA A OPÇÃO DESEJADA: ')
    if opcao_usuario == "1":
        limpa()
        menu_cadastros()
    elif opcao_usuario == "2":
        limpa()
        menu_consultas()
    elif opcao_usuario == "3":
        limpa()
        menu_inserir_credito()
    elif opcao_usuario == "4":
        limpa()
        menu_deletar()
    elif opcao_usuario == "5":
        limpa()
        print('Obrigado, Volte Sempre!')
        quit()
    elif opcao_usuario > "5" or opcao_usuario <= "0":
        print('Opção inválida, tente novamente!')
        limpa()
        menu_principal()

def menu_cadastros():
    print("\n")
    print(" ---- MENU DE CADASTROS ----")
    print('[1] CADASTRAR USUÁRIO')
    print('[2] CADASTRAR MOTORISTA') 
    print('[3] CADASTRAR CARTÃO')
    print('[4] CADASTRAR ÔNIBUS')
    print('[5] MENU PRINCIPAL')
    opcao_usuario2 = input('\n ESCOLHA A OPÇÃO DESEJADA:')
    if opcao_usuario2 == "1":
        limpa()
        criar_usuario()
        delay(2)
        limpa()
        get_usuario()
        menu_principal()
    elif opcao_usuario2 == "2":
        limpa()
        criar_motorista()
        delay(2)
        limpa()
        get_motorista()
        menu_principal()
    elif opcao_usuario2 == "3":
        limpa()
        get_usuario()
        criar_cartao(menu_principal)
        delay(2)
        limpa()
        get_cartao()
        menu_principal()
    elif opcao_usuario2 == "4":
        limpa()
        criar_onibus()
        delay(2)
        limpa()
        get_onibus()
        menu_principal()
    elif opcao_usuario2 == "5":
        limpa()
        menu_principal()
    elif opcao_usuario2 > "5" or opcao_usuario2 <= "0":
        limpa()
        print('Opção inválida, tente novamente!')
        menu_cadastros()

def menu_consultas():
    print("\n")
    print(" ---- MENU DE CONSULTAS ----")
    print('[1] VISUALIZAR USUÁRIOS')
    print('[2] VISUALIZAR CARTÕES')
    print('[3] VISUALIZAR MOTORISTAS')
    print('[4] VISUALIZAR FROTA DE ÔNIBUS')
    print('[5] MENU PRINCIPAL')
    opcao_usuario3 = input('\n ESCOLHA A OPÇÃO DESEJADA:')
    if opcao_usuario3 == "1":
        limpa()
        get_usuario()
        delay(1)
        menu_principal()
    elif opcao_usuario3 == "2":
        limpa()
        get_cartao()
        delay(1)
        menu_principal()
    elif opcao_usuario3 == "3":
        limpa()
        get_motorista()
        delay(1)
        menu_principal()
    elif opcao_usuario3 == "4":
        limpa()
        get_onibus()
        delay(1)
        menu_principal()
    elif opcao_usuario3 == "5":
        limpa()
        print('x')
        menu_principal()
    elif opcao_usuario3 > "5" or opcao_usuario3 <= "0":
        limpa()
        print('Opção inválida, tente novamente!')
        menu_consultas()

def menu_inserir_credito():
    limpa()
    get_cartao()
    inserir_credito()
    delay(2.5)
    limpa()
    get_cartao()
    menu_principal()    

def menu_deletar():
    print("\n")
    print(" ---- MENU EXCLUSÃO ----")
    print('[1] DELETAR USUÁRIO')
    print('[2] DELETAR MOTORISTA')
    print('[3] DELETAR CARTÃO')
    print('[4] DELETAR ÔNIBUS')
    print('[5] MENU PRINCIPAL')
    opcao_usuario5 = input('\n ESCOLHA A OPÇÃO DESEJADA:')
    if opcao_usuario5 == "1":
        limpa()
        get_usuario()
        deletar_usuario(conex, menu_principal)
        delay(1)
        get_usuario()
        menu_principal()
    elif opcao_usuario5 == "2":
        limpa()
        get_motorista()
        deletar_motorista(conex, menu_principal)
        delay(1)
        get_motorista()
        menu_principal()
    elif opcao_usuario5 == "3":
        limpa()
        get_cartao()
        deletar_cartao(conex, menu_principal)
        delay(1)
        get_cartao()
        menu_principal()
    elif opcao_usuario5 == "4":
        limpa()
        get_onibus()
        deletar_onibus(conex, menu_principal)
        delay(1)
        get_onibus()
        menu_principal()
    elif opcao_usuario5 == "5":
        limpa()
        menu_principal()
    elif opcao_usuario5 > "5" or opcao_usuario5 <= "0":
        limpa()
        print('Opção inválida, tente novamente!')
        menu_deletar()


menu_principal()