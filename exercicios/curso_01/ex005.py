# 5 -  Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
import os

os.system('cls')
valor = int(input('Digite um numero: '))
if valor % 2 == 0:
    print('O numero eh par')
else:
    print('O numero eh impar')
print(f'O numero digitado foi: {valor}')