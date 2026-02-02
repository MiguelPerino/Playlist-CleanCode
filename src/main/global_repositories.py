"""
Repositórios Globais do Sistema
Este arquivo centraliza todos os repositórios para garantir que
músicas e playlists compartilhem os mesmos dados em memória.
"""

from src.models.repositories.musics_repositories import MusicsRepository
from src.models.repositories.playlist_repositories import PlaylistRepository

# Repositórios globais - instanciados UMA ÚNICA VEZ
# Todos os constructors devem importar daqui!
music_repository = MusicsRepository()
playlist_repository = PlaylistRepository()
