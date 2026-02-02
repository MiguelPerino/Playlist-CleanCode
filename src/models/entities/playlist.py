class Playlist:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.__songs = []  # Lista privada de músicas
    
    def add_song(self, song) -> None:
        """Adiciona uma música à playlist"""
        if song not in self.__songs:
            self.__songs.append(song)
    
    def remove_song(self, song_title: str) -> bool:
        """Remove uma música da playlist pelo título"""
        for song in self.__songs:
            if song.title == song_title:
                self.__songs.remove(song)
                return True
        return False
    
    def get_songs(self) -> list:
        """Retorna cópia da lista de músicas"""
        return self.__songs.copy()
    
    def get_song_count(self) -> int:
        """Retorna quantidade de músicas na playlist"""
        return len(self.__songs)

        