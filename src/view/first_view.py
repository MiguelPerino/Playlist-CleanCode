def introduction_page() -> str:
    message = '''
    🎵 Sistema Musical
    
    === MÚSICAS ===
    1 - Cadastrar música
    
    === PLAYLISTS ===
    2 - Criar playlist
    3 - Adicionar música à playlist
    4 - Listar playlists
    
    === SISTEMA ===
    0 - Sair
    '''

    print(message)
    command = input('Opção: ')
    return command