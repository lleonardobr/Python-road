import os

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('1. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    #os.system('clear') no mac
    print('Finalizando o app....\n')

def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opcao: '))
    #opcao_escolhida = int(opcao_escolhida)
    if opcao_escolhida == 1:
        print('Cadastrar Restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurane')
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()