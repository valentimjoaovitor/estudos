'''atividade 8.7 Álbum página 189'''
def make_album(author_name, album_name, numero_de_musicas=None):
    album = {
        'Artista: ': author_name,
        'Album: ': album_name,
        'quantidade': numero_de_musicas
    }


    if numero_de_musicas:
        print(album)
    else:
        print(album)

album1 = make_album('sid', 'poesias e frustrações', 15)
album2 = make_album('McDonalds', 'rapDoLanche')