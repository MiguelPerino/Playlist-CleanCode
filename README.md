🎵 Playlist Manager - Clean Code & MVC
Este projeto é um sistema de gerenciamento de músicas e playlists desenvolvido em Python. O objetivo principal deste repositório, além da funcionalidade, é demonstrar a aplicação de boas práticas de programação (Clean Code) e a organização de software utilizando o padrão de arquitetura MVC (Model-View-Controller).

🚀 Funcionalidades
Cadastrar Músicas: Inserção de novas faixas no sistema com detalhes específicos.

Criar Playlists: Agrupamento de músicas em listas personalizadas.

Interface via Terminal: Navegação intuitiva através de comandos numéricos.

🏗️ Arquitetura e Estrutura
O projeto segue o padrão MVC, separando as responsabilidades de forma clara:

Model (src/models): Contém a lógica de dados e a comunicação com o "banco de dados" (neste caso, repositórios). Inclui as entidades (entities) e a lógica de persistência (repositories).

View (src/view): Responsável por toda a interação com o usuário. Nenhuma lógica de negócio reside aqui, apenas comandos de entrada (input) e saída (print).

Controller (src/controllers): O "cérebro" da aplicação. Faz a ponte entre a View e o Model, processando as requisições e validando as regras de negócio.

Estrutura de Pastas:
```plaintext
  src/
  ├── controllers/    # Lógica de controle (ex: song_register_controller)
  ├── main/           # Ponto de entrada e handlers de processo
  ├── models/         # Entidades e Repositórios (banco de dados)
  └── view/           # Interfaces de usuário (telas do terminal)
  run.py              # Arquivo de inicialização do sistema
```

🧼 Clean Code Aplicado
Neste projeto, foram aplicados diversos conceitos do livro Clean Code de Robert C. Martin:

Nomes Significativos: Variáveis, funções e classes possuem nomes que revelam sua intenção (ex: song_register_process, introduction_page).

Funções Pequenas e Únicas (SRP): Cada função ou classe tenta realizar apenas uma tarefa de forma concisa.

Separação de Preocupações: O uso do MVC garante que a lógica de interface não se misture com a lógica de dados.

Classes Coesas: Utilização de Programação Orientada a Objetos para agrupar dados e comportamentos de forma lógica.

Injeção de Dependência: Facilitando a manutenção e os testes futuros (visto nos construtores).

## 🛠️ Como Executar

Para rodar o projeto localmente, siga os passos abaixo no seu terminal:

```bash
# 1. Clone o repositório
git clone https://github.com/MiguelPerino/Playlist-CleanCode.git

# 2. Entre na pasta do projeto
cd Playlist-CleanCode

# 3. Execute a aplicação
python run.py
```
