class Carro:
    carros = []

    def __init__(self, modelo='', marca='', cor='', ano=''):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
    
    def __str__(self):
        return f'{self.modelo} | {self.marca} | {self.cor} | {self.ano}'
    
    def listar_carros():
        for carro in carros:
            print({f'({carro.modelo}) | {carro.marca} | {carro.cor} | {carro.ano}'})

carro1 = Carro('Gol','Volks','2023','Branco')
carro2 = Carro('Polo','Volks','2023','Branco')
carro3 = Carro('Golf','Volks','2023','Vermelho')
carro4 = Carro('Tiguan','Volks','2023','Preto')

carros =[carro1,carro2,carro3,carro4]


Carro.listar_carros()