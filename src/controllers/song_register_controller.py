from src.models.entities.music import Music
from src.models.repositories.musics_repositories import MusicsRepository

class SongRegisterController:
    def __init__(self, music_repo: MusicsRepository):
        self.__music_repo = music_repo

    def insert(self, new_song_informations: dict) -> dict:
        #Princípio da responsabilidade única
        try:
            self.__verify_song_infos(new_song_informations)  
            self.__verify_if_song_already_registered(new_song_informations)
            self.__insert_song(new_song_informations)
            return self.__format_response(new_song_informations)
        except Exception as exception:
            return self.__format_error_response(exception)

    def __verify_song_infos(self, new_song_informations: dict) -> None:
        if len(new_song_informations['title']) > 100:
            raise Exception('Titulo de música com mais de 100 caracteres')
        
        year = int(new_song_informations['year'])
        if year >= 2026:
            raise Exception('Ano de música inválido!')
        


    def __verify_if_song_already_registered(self, new_song_informations: dict) -> None:
        existing_song = self.__music_repo.find_music(new_song_informations['title'])
        
        if existing_song:
            raise Exception(f'A música "{new_song_informations["title"]}" já está cadastrada!')

    def __insert_song(self, new_song_informations: dict) -> None:
        new_music = Music(
            title=new_song_informations['title'],
            artist=new_song_informations['artist'],
            year=int(new_song_informations['year'])
        )
        
        self.__music_repo.insert_music(new_music)

    def __format_response(self, new_song_informations: dict) -> dict:
        return {
            'success': True,
            'count': 1,
            'attributes': {
                'title': new_song_informations['title']
            }
        }

    def __format_error_response(self, err: Exception) -> dict:
        return {
            'success': False,
            'error': str(err)
        }