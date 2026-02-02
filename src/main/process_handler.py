from src.view.first_view import introduction_page
from .constructor.song_register_constructor import song_register_process
from .constructor.playlist_constructor import (
    create_playlist_process,
    add_song_to_playlist_process,
    list_playlists_process
)

def start() -> None:
    while True:
        command = introduction_page()
        
        if command == '1': 
            song_register_process()
        elif command == '2': 
            create_playlist_process()
        elif command == '3': 
            add_song_to_playlist_process()
        elif command == '4': 
            list_playlists_process()
        elif command == '0': 
            print('\nAté logo!\n')
            exit()
        else: 
            print('\n⚠️  Comando não encontrado, tente novamente...\n')
