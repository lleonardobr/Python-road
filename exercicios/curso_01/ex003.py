#3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
import os
import time

print('A')
print('L')
print('U')
print('R')
print('A')


print('Este foi o primeiro exemplo.')
print('Vamos preparar a segunda forma de exibir com utilizando um FOR: ')

time.sleep(5)
os.system('cls')
palavra = 'ALURA'
for letra in palavra:
    print(letra)


print('A','L','U','R','A',sep='\n')
