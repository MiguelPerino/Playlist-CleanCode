# 🎵 Playlist Manager - Clean Code & MVC

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Clean Code](https://img.shields.io/badge/clean%20code-yes-brightgreen.svg)
![MVC](https://img.shields.io/badge/architecture-MVC-orange.svg)

*Sistema de gerenciamento de músicas e playlists desenvolvido com foco em Clean Code e Arquitetura MVC*

[Funcionalidades](#-funcionalidades) •
[Arquitetura](#️-arquitetura) •
[Instalação](#️-instalação) •
[Princípios](#-clean-code-aplicado) •
[Contribuir](#-contribuindo)

</div>

---

## 📖 Sobre o Projeto

Este projeto é um **sistema de gerenciamento de músicas e playlists** desenvolvido em Python. O objetivo principal, além da funcionalidade, é **demonstrar a aplicação de boas práticas de programação** (Clean Code) e a organização de software utilizando o padrão de arquitetura **MVC** (Model-View-Controller).

### 🎯 Objetivos de Aprendizado

- ✅ Aplicar princípios de **Clean Code** de Robert C. Martin
- ✅ Implementar arquitetura **MVC** de forma clara e organizada
- ✅ Praticar **Programação Orientada a Objetos**
- ✅ Utilizar **Injeção de Dependências**
- ✅ Separar responsabilidades seguindo o **Single Responsibility Principle**

---

## ✨ Funcionalidades

### 🎼 Gerenciamento de Músicas
- **Cadastrar Músicas**: Adicione novas faixas ao sistema com título, artista e ano
- **Validação de Dados**: Verificação automática de informações (título, ano válido)
- **Prevenção de Duplicatas**: Sistema impede cadastro de músicas duplicadas

### 📝 Gerenciamento de Playlists
- **Criar Playlists**: Crie playlists personalizadas com nome e descrição
- **Adicionar Músicas**: Adicione músicas cadastradas às suas playlists
- **Listar Playlists**: Visualize todas as playlists com suas músicas
- **Validação Completa**: Verificações de existência e integridade de dados

### 💻 Interface
- **Terminal Interativo**: Navegação simples através de menu numérico
- **Feedback Visual**: Mensagens claras de sucesso e erro
- **User-Friendly**: Interface intuitiva e fácil de usar

---

## 🏗️ Arquitetura

O projeto segue rigorosamente o padrão **MVC**, garantindo separação clara de responsabilidades:

### 📂 Estrutura de Pastas

```
Playlist-CleanCode/
│
├── src/
│   ├── models/                    # 📊 MODEL - Camada de Dados
│   │   ├── entities/              # Entidades do domínio
│   │   │   ├── music.py          # Entidade Música
│   │   │   └── playlist.py       # Entidade Playlist
│   │   └── repositories/          # Camada de Persistência
│   │       ├── musics_repositories.py
│   │       └── playlist_repositories.py
│   │
│   ├── controllers/               # 🧠 CONTROLLER - Lógica de Negócio
│   │   ├── song_register_controller.py
│   │   └── playlist_controller.py
│   │
│   ├── view/                      # 🖥️ VIEW - Interface do Usuário
│   │   ├── first_view.py         # Menu principal
│   │   ├── song_register_view.py # Telas de música
│   │   ├── playlist_register_view.py
│   │   ├── playlist_add_song_view.py
│   │   └── playlist_list_view.py
│   │
│   └── main/                      # 🔧 Configuração e Orquestração
│       ├── repositories.py       # Repositórios globais (Single Source of Truth)
│       ├── process_handler.py    # Handler principal
│       └── constructor/          # Injeção de dependências
│           ├── song_register_constructor.py
│           └── playlist_constructor.py
│
└── run.py                         # 🚀 Ponto de entrada da aplicação
```

### 🎯 Responsabilidades de Cada Camada

#### 📊 MODEL (Modelos)
- **Entities**: Representam os objetos do domínio (Music, Playlist)
- **Repositories**: Simulam banco de dados, gerenciam persistência
- **Responsabilidade**: Apenas dados e lógica de acesso a dados

#### 🧠 CONTROLLER (Controladores)
- Recebe requisições das Views
- Aplica regras de negócio e validações
- Orquestra comunicação entre View e Model
- Retorna respostas formatadas
- **Responsabilidade**: Lógica de negócio e validações

#### 🖥️ VIEW (Visualizações)
- Exibe informações ao usuário
- Coleta inputs do usuário
- **SEM lógica de negócio**
- **Responsabilidade**: Apenas interface e interação

---

## 🛠️ Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Git

### Passos para Executar

```bash
# 1. Clone o repositório
git clone https://github.com/MiguelPerino/Playlist-CleanCode.git

# 2. Entre na pasta do projeto
cd Playlist-CleanCode

# 3. Execute a aplicação
python run.py
```

### 🎮 Como Usar

1. **Cadastrar uma música**
   - Escolha opção `1`
   - Informe título, artista e ano
   
2. **Criar uma playlist**
   - Escolha opção `2`
   - Defina nome e descrição
   
3. **Adicionar música à playlist**
   - Escolha opção `3`
   - Informe nome da playlist e título da música
   
4. **Listar playlists**
   - Escolha opção `4`
   - Visualize todas as playlists com suas músicas

---

## 🧼 Clean Code Aplicado

Este projeto implementa diversos princípios do livro **"Clean Code"** de Robert C. Martin:

### 1️⃣ **Nomes Significativos**
```python
# ✅ Bom - auto-explicativo
def create_playlist(self, playlist_info: dict) -> dict:
    ...

# ❌ Evitado - nome genérico
def process(self, data):
    ...
```

### 2️⃣ **Single Responsibility Principle (SRP)**
```python
# Cada método tem UMA responsabilidade
def __validate_playlist_info(self, info: dict) -> None:
    """Apenas valida informações"""
    
def __check_if_playlist_exists(self, name: str) -> None:
    """Apenas verifica existência"""
    
def __insert_song(self, song_info: dict) -> None:
    """Apenas insere no repositório"""
```

### 3️⃣ **Funções Pequenas**
- Métodos focados e concisos
- Cada função faz apenas uma coisa
- Fácil leitura e manutenção

### 4️⃣ **Separação de Preocupações**
- MVC garante que interface não se misture com lógica
- Cada camada tem responsabilidade bem definida

### 5️⃣ **Injeção de Dependências**
```python
class PlaylistController:
    def __init__(self, playlist_repo: PlaylistRepository, music_repo: MusicsRepository):
        self.__playlist_repo = playlist_repo
        self.__music_repo = music_repo
```

### 6️⃣ **Encapsulamento**
```python
class Playlist:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.__songs = []  # Atributo privado
    
    def get_songs(self) -> list:
        return self.__songs.copy()  # Retorna cópia, não referência
```

### 7️⃣ **Tratamento de Erros Consistente**
```python
try:
    self.__validate_playlist_info(playlist_info)
    self.__check_if_playlist_exists(playlist_info['name'])
    # ... lógica
    return self.__format_success_response(new_playlist)
except Exception as error:
    return self.__format_error_response(error)
```

### 8️⃣ **Single Source of Truth**
```python
# repositories.py - UM ÚNICO lugar para instanciar repositórios
music_repository = MusicsRepository()
playlist_repository = PlaylistRepository()
```

---

## 🎨 Padrões de Design Utilizados

### 🏭 **Repository Pattern**
- Abstrai a lógica de persistência
- Separa acesso a dados da lógica de negócio
- Facilita troca de "banco de dados"

### 💉 **Dependency Injection**
- Controllers recebem dependências via construtor
- Facilita testes unitários
- Reduz acoplamento

### 🎯 **MVC Pattern**
- Separação clara de responsabilidades
- Fácil manutenção e escalabilidade
- Código organizado e limpo

---

## 📚 Aprendizados e Conceitos

### 🔑 Conceitos-Chave Implementados

| Conceito | Aplicação no Projeto |
|----------|---------------------|
| **SOLID - SRP** | Cada classe/método tem uma única responsabilidade |
| **SOLID - DIP** | Controllers dependem de abstrações (repositories) |
| **DRY** | Código não repetitivo, métodos reutilizáveis |
| **KISS** | Soluções simples e diretas |
| **Fail Fast** | Validações no início, erros lançados cedo |
| **Encapsulation** | Atributos privados, acesso controlado |

### 📖 Referências e Inspirações

- **Clean Code** - Robert C. Martin
- **Design Patterns** - Gang of Four
- **The Pragmatic Programmer** - Andrew Hunt & David Thomas
- **Python Best Practices** - PEP 8

---

## 🚀 Possíveis Melhorias Futuras

- [ ] Persistência em banco de dados (SQLite/PostgreSQL)
- [ ] Interface gráfica (Tkinter/PyQt)
- [ ] Testes unitários com pytest
- [ ] API REST com Flask/FastAPI
- [ ] Sistema de busca avançada
- [ ] Ordenação de playlists
- [ ] Edição e remoção de músicas/playlists
- [ ] Exportação de playlists (JSON/CSV)
- [ ] Sistema de favoritos
- [ ] Histórico de reprodução

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Este é um projeto educacional, então sinta-se à vontade para:

1. 🍴 Fork o projeto
2. 🌿 Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. 💾 Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. 📤 Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. 🔃 Abra um Pull Request

### 📝 Diretrizes para Contribuição

- Mantenha os princípios de Clean Code
- Siga a arquitetura MVC estabelecida
- Adicione comentários quando necessário
- Mantenha nomenclatura em português (padrão do projeto)
- Teste suas mudanças antes de submeter

---

## 👨‍💻 Autor

**Miguel Perino**

- GitHub: [@MiguelPerino](https://github.com/MiguelPerino)
- LinkedIn: [[@MiguelPerino](https://www.linkedin.com/in/miguel-perino/)]
- Email: [miguelcperino@gmail.com]

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙏 Agradecimentos

- Robert C. Martin pelo livro "Clean Code"
- Comunidade Python pela excelente documentação
- Todos que contribuírem para este projeto

---

<div align="center">

**⭐ Se este projeto te ajudou de alguma forma, considere dar uma estrela! ⭐**



</div>
