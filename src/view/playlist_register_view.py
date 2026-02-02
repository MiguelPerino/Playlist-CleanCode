import os

class PlaylistRegisterView:
    def get_playlist_info(self) -> dict:
        """Coleta informações para criar playlist"""
        self.__clear()
        print('=== CRIAR NOVA PLAYLIST ===\n')
        
        name = input('Nome da playlist: ')
        description = input('Descrição (opcional): ')
        
        return {
            'name': name,
            'description': description
        }
    
    def show_success(self, response: dict) -> None:
        """Exibe mensagem de sucesso"""
        self.__clear()
        
        attrs = response['attributes']
        message = f'''
        ✓ Playlist criada com sucesso!
        
        Nome: {attrs['name']}
        Descrição: {attrs['description'] or 'Nenhuma'}
        Músicas: {attrs['song_count']}
        '''
        
        print(message)
        input('\nPressione ENTER para continuar...')
    
    def show_error(self, response: dict) -> None:
        """Exibe mensagem de erro"""
        self.__clear()
        
        message = f'''
        ✗ Erro ao criar playlist!
        
        Erro: {response['error']}
        '''
        
        print(message)
        input('\nPressione ENTER para continuar...')
    
    def __clear(self):
        os.system("cls||clear")
