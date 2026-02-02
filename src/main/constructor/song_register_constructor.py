from src.main.global_repositories import music_repository  # ← IMPORTA DO CENTRALIZADOR
from src.controllers.song_register_controller import SongRegisterController
from src.view.song_register_view import SongRegisterView

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