from src.models.entities.playlist import Playlist
from src.models.repositories.playlist_repositories import PlaylistRepository
from src.models.repositories.musics_repositories import MusicsRepository

class PlaylistController:
    def __init__(self, playlist_repo: PlaylistRepository, music_repo: MusicsRepository):
        self.__playlist_repo = playlist_repo
        self.__music_repo = music_repo
    
    def create_playlist(self, playlist_info: dict) -> dict:

        try:
            self.__validate_playlist_info(playlist_info)
            self.__check_if_playlist_exists(playlist_info['name'])
            
 
            new_playlist = Playlist(
                name=playlist_info['name'],
                description=playlist_info.get('description', '')
            )
            
            self.__playlist_repo.insert_playlist(new_playlist)
            return self.__format_success_response(new_playlist)
            
        except Exception as error:
            return self.__format_error_response(error)
    
    def add_song_to_playlist(self, data: dict) -> dict:

        try:
            playlist_name = data['playlist_name']
            song_title = data['song_title']
            
            # Busca playlist e música
            playlist = self.__playlist_repo.find_playlist_by_name(playlist_name)
            if not playlist:
                raise Exception(f'Playlist "{playlist_name}" não encontrada!')
            
            song = self.__music_repo.find_music(song_title)
            if not song:
                raise Exception(f'Música "{song_title}" não encontrada!')
            
            playlist.add_song(song)
            
            return {
                'success': True,
                'message': f'Música "{song_title}" adicionada à playlist "{playlist_name}"!',
                'song_count': playlist.get_song_count()
            }
            
        except Exception as error:
            return self.__format_error_response(error)
    
    def list_playlists(self) -> dict:
        try:
            playlists = self.__playlist_repo.get_all_playlists()
            
            return {
                'success': True,
                'playlists': playlists,
                'count': len(playlists)
            }
        except Exception as error:
            return self.__format_error_response(error)
    
    # Métodos privados de validação
    def __validate_playlist_info(self, info: dict) -> None:
        if not info.get('name'):
            raise Exception('Nome da playlist é obrigatório!')
        
        if len(info['name']) > 50:
            raise Exception('Nome muito longo! Máximo 50 caracteres.')
        
        if info.get('description') and len(info['description']) > 200:
            raise Exception('Descrição muito longa! Máximo 200 caracteres.')
    
    def __check_if_playlist_exists(self, name: str) -> None:
        existing = self.__playlist_repo.find_playlist_by_name(name)
        if existing:
            raise Exception(f'Já existe uma playlist com o nome "{name}"!')
    
    def __format_success_response(self, playlist: Playlist) -> dict:
        return {
            'success': True,
            'message': 'Playlist criada com sucesso!',
            'attributes': {
                'name': playlist.name,
                'description': playlist.description,
                'song_count': playlist.get_song_count()
            }
        }
    
    def __format_error_response(self, error: Exception) -> dict:
        return {
            'success': False,
            'error': str(error)
        }
