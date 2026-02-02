from src.models.repositories.musics_repositories import MusicsRepository
from src.controllers.song_register_controller import SongRegisterController
from src.view.song_register_view import SongRegisterView

# Repositório global de músicas (compartilhado com playlist)
music_repository = MusicsRepository()

def song_register_process():
    # Instancia componentes com injeção de dependência
    controller = SongRegisterController(music_repository)
    view = SongRegisterView()
    
    new_song_informations = view.registry_song_initial()
    
    response = controller.insert(new_song_informations)
    
    if response['success']:
        view.registry_song_success(response)
    else:
        view.registry_song_fail(response)