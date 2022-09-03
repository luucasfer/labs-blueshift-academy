#BIBLIOTECAS
from colorama import Fore, Back, Style


#VARIÁVEIS PARA RELATÓRIO
assentos_ocupados = []
corredor = []


#FUNÇÃO DE DECORAÇÃO
def firulas():
    print(f'{Fore.BLACK}{Back.GREEN}={Style.RESET_ALL}'*21)


#CRIAR A MATRIZ PRINCIPAL
def criar_matriz(n_linhas, n_colunas):
    matriz = []
    v = 1
    for x in range(n_linhas):
        linhas = []
        for y in range(n_colunas):
            linhas.append(v)
            v += 1
        matriz.append(linhas)
    return matriz


#CRIA O CORREDOR
def assentos_corredor(matriz_onibus):
    metade_matriz = int(len(matriz_onibus[0]) // 2)
    for i in range(len(matriz_onibus[0])):
        x = matriz_onibus[0][i]
        corredor.append(x)
    for j in range(len(matriz_onibus)):
        y = matriz_onibus[j][metade_matriz]
        corredor.append(y)
    return corredor


#FUNÇÃO BOAS VINDAS
def boas_vindas():
    firulas()
    print(f'{Fore.BLACK}{Back.GREEN}BEM VINDO AO POCCOBUS{Style.RESET_ALL}')
    firulas()


#FUNÇÃO OPÇÕES
def opcoes():
    print(f'{Fore.BLACK}{Back.LIGHTYELLOW_EX}[1] RESERVAR ASSENTO {Style.RESET_ALL}')
    print(f'{Fore.BLACK}{Back.LIGHTYELLOW_EX}[2] EMITIR RELATÓRIO {Style.RESET_ALL}')
    print(f'{Fore.BLACK}{Back.LIGHTYELLOW_EX}[3] SAIR             {Style.RESET_ALL} \n')
    opcao_usuario = input('ESCOLHA A OPÇÃO DESEJADA (1, 2 ou 3):')

    if opcao_usuario == "1":
        colorir()
        reserva_assento()
    elif opcao_usuario == "2":
        relatorio()
        print(f'{Fore.BLACK}{Back.GREEN}O Relatório foi emitido!{Style.RESET_ALL} \n')
        opcoes()
    elif opcao_usuario == "3":
        print(f'{Fore.BLACK}{Back.GREEN}OBRIGADO, Volte Sempre!{Style.RESET_ALL} \n')
        quit()
    elif opcao_usuario != "1" or "2" or "3":
        print(f'{Fore.BLACK}{Back.LIGHTRED_EX}Opção inválida, tente novamente!{Style.RESET_ALL} \n')
        opcoes()


#FUNÇÃO RESERVAR ASSENTO
def reserva_assento():
    #global assentos_ocupados
    while True:
        entrada = int(input("ESCOLHA O NÚMERO DO ASSENTO QUE DESEJA: "))
        tamanho_matriz = (len(onibus) * len(onibus[0]))  #Multiplica a quantidade de linhas e colunas da matriz
        if (entrada > 0 and entrada <= tamanho_matriz) and (entrada not in corredor) and (entrada not in assentos_ocupados):
            print(f'{Fore.BLACK}{Back.GREEN}O assento {entrada} foi reservado! {Style.RESET_ALL} \n')
            assentos_ocupados.append(entrada)
            colorir()
            novos_assentos()
        elif (entrada > 0 and entrada <= tamanho_matriz) and (entrada not in corredor) and (entrada in assentos_ocupados):
            print(f'{Fore.BLACK}{Back.LIGHTRED_EX}O assento {entrada} já está reservado {Style.RESET_ALL} \n')
        else:
            print(f'{Fore.BLACK}{Back.LIGHTRED_EX}{entrada} não é um número válido! {Style.RESET_ALL} \n')
            reserva_assento()


#FUNÇÃO RESERVAR MAIS ASSENTOS
def novos_assentos():
    while True:
        novo_assento = str(input("\n DESEJA RESERVAR MAIS UM ASSENTO? (S/N) "))
        if novo_assento == "S" or novo_assento == "s":
            reserva_assento()
        elif novo_assento == "N" or novo_assento == "n":
            opcoes()
        elif novo_assento != "S" or "s" or "N" or "n":
            print(f'{Fore.BLACK}{Back.LIGHTRED_EX}Opção inválida!{Style.RESET_ALL} \n')
            novos_assentos()




#FUNÇÃO EMITIR RELATÓRIO
def relatorio ():
    arquivo = open('relatorio.txt', 'w')
    res = []
    livre = []
    for item in assentos_livres:
        if item in assentos_ocupados:
            res.append(item)
        elif item in assentos_livres and item not in corredor:
            livre.append(item)
    res.sort()
    livre.sort()
    arquivo.write(f'Assentos Reservados = {res} \n')
    arquivo.write(f'Assentos Disponíveis = {livre} ')
    arquivo.close()



#FUNÇÃO COR DOS ASSENTOS
def colorir():
    print(f'\n ')
    print(f'{Fore.BLACK}{Back.GREEN}  {Style.RESET_ALL} Disponíveis')
    print(f'{Fore.BLACK}{Back.LIGHTRED_EX}  {Style.RESET_ALL} Indisponíveis')
    print(f'{Fore.BLACK}{Back.BLACK}  {Style.RESET_ALL} Corredor')
    print(f'{Fore.BLACK}{Back.LIGHTBLUE_EX}  {Style.RESET_ALL} Motorista\n')
    for linha in onibus:
        for elemento in linha:
            if elemento == onibus[0][0]:
                print(f'{Fore.BLACK}{Back.LIGHTBLUE_EX}{elemento}{Style.RESET_ALL}', end='\t')
            elif elemento in corredor:
                print(f'{Fore.WHITE}{Back.BLACK}{elemento}{Style.RESET_ALL}', end='\t')
            elif elemento in assentos_ocupados:
                print(f'{Fore.BLACK}{Back.LIGHTRED_EX}{elemento}{Style.RESET_ALL}', end='\t')
            else:
                print(f'{Fore.BLACK}{Back.GREEN}{elemento }{Style.RESET_ALL}', end='\t')
        print()


onibus = criar_matriz(8, 5)
tamanho_matriz = (len(onibus) * len(onibus[0]))
assentos_livres = list(range(1,tamanho_matriz + 1))
assentos_corredor(onibus)
boas_vindas()
opcoes()





