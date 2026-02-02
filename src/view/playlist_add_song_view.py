import os

class PlaylistAddSongView:
    def get_add_song_info(self) -> dict:
        """Coleta informações para adicionar música"""
        self.__clear()
        print('=== ADICIONAR MÚSICA À PLAYLIST ===\n')
        
        playlist_name = input('Nome da playlist: ')
        song_title = input('Título da música: ')
        
        return {
            'playlist_name': playlist_name,
            'song_title': song_title
        }
    
    def show_success(self, response: dict) -> None:
        self.__clear()
        
        message = f'''
        ✓ {response['message']}
        
        Total de músicas na playlist: {response['song_count']}
        '''
        
        print(message)
        input('\nPressione ENTER para continuar...')
    
    def show_error(self, response: dict) -> None:
        self.__clear()
        
        message = f'''
        ✗ Erro ao adicionar música!
        
        Erro: {response['error']}
        '''
        
        print(message)
        input('\nPressione ENTER para continuar...')
    
    def __clear(self):
        os.system("cls||clear")
