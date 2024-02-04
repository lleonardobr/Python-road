from modelos.restaurante import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0 ,'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'o melhor pao da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()