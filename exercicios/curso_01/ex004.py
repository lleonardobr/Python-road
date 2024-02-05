#4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:

import os

pi = 3.14159265358979323846

os.system('cls')
print("Número arredondado:", round(pi, 2))
print(f"Número arredondado: {round(pi, 2)}")
print(f"Número arredondado: {pi:.2f}")

pi = round(pi, 3)
print('O ultimo valor com 3 casa decimais:', pi)


#Correcao Alura:
pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))
