'''atividade 8.8 Álbuns de usuários página 189'''

def make_album(artist, album_name):
    print("\nSeu artista e album favorito é:")
    favoritos = f"Artista: {artist}\
        Album: {album_name}"
    
    print(favoritos)
    return favoritos

while True:
    print('\ndigite "q" em uma das perguntas para sair.')
    art_name = input('Coloque o nome do seu artista favorito: ')

    if art_name == 'q':
        break

    alb_name = input('Coloque o nome do seu album favorito: ')

    if alb_name == 'q':
        break
    
    make_album(art_name, alb_name)
