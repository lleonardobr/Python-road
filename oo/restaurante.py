class Restaurante:
    restaurantes = []

    def __init__(self, nome='', categoria=''):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__():
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

    @property
    def ativo(self): 
        return 'verdadeiro' if self.ativo else 'false'
    
restaurante_praca = Restaurante('teste_praca', 'Testando')
restaurante_pizza = Restaurante('Tenste_pizza', 'Gourmulet')


