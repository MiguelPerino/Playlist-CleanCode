from src.models.entities.playlist import Playlist

class PlaylistRepository:
    def __init__(self):
        self.__playlists = []
    
    def insert_playlist(self, playlist: Playlist) -> None:
        self.__playlists.append(playlist)
    
    def find_playlist_by_name(self, name: str) -> Playlist:
        for playlist in self.__playlists:
            if playlist.name == name:
                return playlist
        return None
    
    def get_all_playlists(self) -> list:
        return self.__playlists.copy()
    
    def delete_playlist(self, name: str) -> bool:
        playlist = self.find_playlist_by_name(name)
        if playlist:
            self.__playlists.remove(playlist)
            return True
        return False
