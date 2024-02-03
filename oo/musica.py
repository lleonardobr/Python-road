class Musica:
    nome = ''
    banda = '' 
    duracao = ''

musica_01 = Musica()
musica_01.nome = 'Shape of you'
musica_01.banda = 'Ed Sheeran'
musica_01.duracao = '4:23'

musica_02 = Musica()
musica_02.nome = 'Blinding Lights'
musica_02.banda = 'The Weeknd'
musica_02.duracao = '3:33'

musica_03 = Musica()
musica_02.nome = 'Bohemian Rhapsody'
musica_02.banda = 'Queen'
musica_02.duracao = '5:55'

playlist = [musica_01,musica_02, musica_03]

print(vars(musica_01))