from src.view.first_view import introduction_page

def start() -> None:
    while True:

        command = introduction_page()
        
        if command == '1': print('inserindo música')
        elif command == '2': print('Criando playlist')
        elif command == '5': exit()
        else: print('\nComando não encontrado, tente novamente...\n')

            
