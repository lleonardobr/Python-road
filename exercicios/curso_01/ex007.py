# 7 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
import os
import time

os.system('cls')
usuario_check = 'delasilva.silva'
password_check = '123321'

usuario = input('Digite o login: ')
password = input('Digite a senha: ')

print('Autenticando....')
time.sleep(5)

def verificar_senha():
    if usuario != usuario_check:
        print('Usuario invalido')
    elif password != password_check:
        print('Senha invalida')
    else:
        print('usuario logado !!!')

verificar_senha()