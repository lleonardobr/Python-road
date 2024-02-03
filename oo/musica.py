class Musica:
    playlist = []

    def __init__(self, nome='', banda='', duracao=''):
        self.nome = nome
        self.banda = banda
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} | {self.banda}'
    
    def listar_restaurantes():
        for musica in Musica.playlist:
            print(f'{musica.nome} | {musica.banda}')

musica_01 = Musica('Shape of you','Ed Sheeran')
musica_02 = Musica('Blinding Ligths','The Weeknd','3:33')
musica_03 = Musica('Bohemian Rhapsody','Queen', '5:55')

playlist = [musica_01,musica_02, musica_03]

print(playlist)