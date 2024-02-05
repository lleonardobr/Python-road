#2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
import os

nome_01 = 'Leonardo'
idade_01 = str(20)
nome_02 = input('Infomre seu nome: ')
idade_02 = input('Informe a sua idade: ')


os.system('cls')
print(f'Nome: {nome_01.ljust(10)} | Idade: {idade_01.ljust(10)}')
print(f'Nome: {nome_02.ljust(10)} | Idade: {idade_02.ljust(10)}')

if idade_01 >= idade_02:
    print(f'(O {nome_01} eh mais velho)')
else:
    print(f'O {nome_02} eh o mais velho')


#Correcao:

# Criação das Variáveis
nome = 'Lais'
idade = 24

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))
