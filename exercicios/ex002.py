#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar
numero = int(input('Digite um numero: '))
print('processing....')
#Você pode verificar se um número é par ou ímpar no Python usando o operador de módulo (%). Se o resultado da divisão por 2 for igual a 0, o número é par; caso contrário, é ímpar. Aqui está um exemplo simples:
if numero & 2 == 0: 
    print(f'O {numero} eh um numero par')
else:
    print(f'O {numero} eh um numero impar')


#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos
idade = int(input('Informe a sua idade: '))

if idade >= 0 and idade <= 12:
    print('Crianca')
elif  idade > 12 and idade <= 18:
    print('Adolescente')
else:
    print('Adulto')


#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
login_allowed = 'cholo'
pass_allowed = '123321'

print('Bem-Vindo\n')
print('Informe o seu login e senha para continuar...')
login = input('Login:')
passwd = input('Password:')


if login == login_allowed and passwd == pass_allowed:
    print(f'{login} O seu login foi realizado com sucesso....')
else:
    print('Login ou senha incorreta!')


#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.


# Solicita ao usuário as coordenadas (x, y)
x = float(input('Informe o valor de X:'))
y = float(input('Informe o valor de y:'))
# Determina em qual quadrante o ponto se encontra

if x > 0 and y > 0:
    print('O ponto esta no Primeio Quadrante')
elif x < 0 and y > 0:    
    print('O ponto esta no Segundo Quadrante')
elif x < 0 and y < 0:
    print('O ponto esta no Terceiro Quadrante') 
elif x > 0 and y < 0:
    print('O ponto esta no Quarto Quadrante')
else:    
    print('O ponto esta no eixo ou na origem')

