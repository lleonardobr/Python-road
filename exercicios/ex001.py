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

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))

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