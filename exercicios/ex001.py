print('Ex001:\n')
print('Python na Escola de Programacao da Alura')


print('Ex002:\n')
nome = input('Nome:')
idade = input('Idade:')
# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

print('Ex003:')
print("""
A
L
U
R
A
\n""")

print('A','L','U','R','A',sep='\n')

print('Ex004\n')
pi = 3.14159
# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))
print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷')

#Outros exercicios que o Luri me recomendou
print('''
      
█░░ █░█ █▀█ █   █▀▄ █▀▀ █▀ ▄▀█ █▀▀ █ █▀█ █▀
█▄▄ █▄█ █▀▄ █   █▄▀ ██▄ ▄█ █▀█ █▀░ █ █▄█ ▄█
''')
print('Luri ex001:')
nome_01  = input('Nome:')
print(f'Bem-vindo {nome_01}')
print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷')
print('Luri ex002:')
nome_02 = input('Nome:')

cidade = input('Cidade onde mora:')
print(f'O usuario {nome_02} mora em {cidade}')
print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷')

print('Luri ex003')
nome_03 = input('Nome:')
idade = int(input('Idade:'))
print(f'O usuario {nome_03} vai ter {idade + 10} anos daqui 10 anos!!!')
print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷')

print('Luri ex004')
nome_completo = input("Digite seu nome completo: ")

# Dividir o nome completo em uma lista de palavras
palavras = nome_completo.split()

# Inicializar uma string vazia para armazenar as iniciais
iniciais = ""

# Percorrer a lista de palavras e adicionar a primeira letra de cada palavra à string de iniciais
for palavra in palavras:
    iniciais += palavra[0]

# Exibir as iniciais
print("As iniciais do seu nome são:", iniciais)


