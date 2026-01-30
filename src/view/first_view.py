def introduction_page() -> str:
    message = '''
        Sistema musical

    * Cadastrar música - 1
    * Criar Playlist - 2
    * Sair - 5
    '''

    print(message)
    command = input('Opção: ')
    return command