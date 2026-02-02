from src.models.repositories.musics_repositories import MusicsRepository
from src.controllers.song_register_controller import SongRegisterController
from src.view.song_register_view import SongRegisterView
from src.models.entities.music import Music

# Repositório global (mesmo usado em playlist_constructor)
music_repository = MusicsRepository()

def song_register_process():
    controller = SongRegisterController()
    view = SongRegisterView()
    
    # Coleta informações
    new_song_informations = view.registry_song_initial()
    
    # Processa
    response = controller.insert(new_song_informations)
    
    # Cria objeto Music e insere no repositório
    if response['success']:
        new_music = Music(
            title=new_song_informations['title'],
            artist=new_song_informations['artist'],
            year=int(new_song_informations['year'])
        )
        music_repository.insert_music(new_music)
        view.registry_song_success(response)
    else:
        view.registry_song_fail(response)