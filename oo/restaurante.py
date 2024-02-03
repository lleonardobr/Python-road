class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praca'
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

print(f'Nome: {restaurante_praca.nome} - Categoria: {restaurante_praca.categoria} - Ativo: {restaurante_praca.ativo}')
print(f'Nome: {restaurante_pizza.nome} - Categoria:{restaurante_pizza.categoria} - Ativo: {restaurante_pizza.ativo}') 


if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria eh fast food')
else:
    print('A categoria nao eh fast food')