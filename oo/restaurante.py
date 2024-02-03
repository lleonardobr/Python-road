class Restaurante:
    restaurantes = []

    def __init__(self, nome='', categoria=''):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__():
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Status".ljust(20)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante._ativo}')

    @property
    def ativo(self): 
        return 'verdadeiro' if self._ativo else 'false'
    
    def alterar_estado(self):
        self._ativo = not self._ativo
    
restaurante_praca = Restaurante('teste_praca', 'Testando')
restaurante_praca.alterar_estado()
restaurante_pizza = Restaurante('Tenste_pizza', 'Gourmulet')


Restaurante.listar_restaurantes()
