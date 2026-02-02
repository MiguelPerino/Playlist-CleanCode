import os

class PlaylistListView:
    def show_playlists(self, response: dict) -> None:
        """Exibe lista de playlists"""
        self.__clear()
        print('=== SUAS PLAYLISTS ===\n')
        
        if response['count'] == 0:
            print('Você ainda não tem playlists criadas.\n')
        else:
            for idx, playlist in enumerate(response['playlists'], 1):
                songs = playlist.get_songs()
                
                print(f'{idx}. {playlist.name}')
                print(f'   Descrição: {playlist.description or "Sem descrição"}')
                print(f'   Músicas: {len(songs)}')
                
                if songs:
                    print('   Faixas:')
                    for song in songs:
                        print(f'      • {song.title} - {song.artist}')
                
                print()
        
        input('Pressione ENTER para voltar...')
    
    def __clear(self):
        os.system("cls||clear")
