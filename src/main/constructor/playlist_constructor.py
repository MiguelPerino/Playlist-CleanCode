from src.models.repositories.playlist_repositories import PlaylistRepository
from src.models.repositories.musics_repositories import MusicsRepository
from src.controllers.playlist_controller import PlaylistController
from src.view.playlist_register_view import PlaylistRegisterView
from src.view.playlist_add_song_view import PlaylistAddSongView
from src.view.playlist_list_view import PlaylistListView

# Repositories globais (simulando banco de dados)
playlist_repository = PlaylistRepository()
music_repository = MusicsRepository()

def create_playlist_process():
    # Instancia componentes
    controller = PlaylistController(playlist_repository, music_repository)
    view = PlaylistRegisterView()
    
    # Coleta dados
    playlist_info = view.get_playlist_info()
    
    # Processa
    response = controller.create_playlist(playlist_info)
    
    # Exibe resultado
    if response['success']:
        view.show_success(response)
    else:
        view.show_error(response)

def add_song_to_playlist_process():
    controller = PlaylistController(playlist_repository, music_repository)
    view = PlaylistAddSongView()
    
    data = view.get_add_song_info()
    response = controller.add_song_to_playlist(data)
    
    if response['success']:
        view.show_success(response)
    else:
        view.show_error(response)

def list_playlists_process():
    controller = PlaylistController(playlist_repository, music_repository)
    view = PlaylistListView()
    
    response = controller.list_playlists()
    view.show_playlists(response)
