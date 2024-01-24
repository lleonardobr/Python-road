#Como já vimos, programação é prática! Criamos mais uma lista de atividades (não obrigatórias) para você exercitar e reforçar ainda mais seu #aprendizado e o conteúdo da vez são listas, blocos de repetição e try except. Bora praticar?

#Exercícios
#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.
def listas():
    lista_numeros = list((range(1,11)))
    lista_nome = ['Leo','Felipe','Andre','Bruno']
    lista_ano = ('1992','2024')

    print('Lista de 1 a 10:')
    for numero in lista_numeros:
        print(numero)

    print('Lista de nomes: ')
    for indice, nome in enumerate(lista_nome):
        print(f'{indice} - {nome}')

    print('Lista ano: ')    
    for ano in lista_ano:
        print(ano)


#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
def listas02():
    listas_numeros02 = [1,2,3,4,5,6]

    print("Elementos da lista")
    for numero in listas_numeros02:
        print(numero)


#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = list(range(1,11))
total = 0

for soma in soma_impares:
    if soma % 2 != 0:
        print(soma)
        total += soma

print(f'a soma total do numeros impares sao: {total}')



#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
def descrescente():
    for numero in range(10, 0 -1):
        print(numero)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
def tabuada():
    tabuada = int(input('Digite um numero: '))

    for i  in range(1, 11):
        print(f'{tabuada} x {i} = {tabuada * i}')

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.



#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

