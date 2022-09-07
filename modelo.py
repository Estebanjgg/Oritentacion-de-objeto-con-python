class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
       return f'{self._nome} - {self.ano}  - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
       return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
      return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
    def __len__(self):
        return len(self._programas)

   

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmpe = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_likes()
tmpe.dar_likes()
tmpe.dar_likes()
tmpe.dar_likes()
tmpe.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, tmpe]
playlist_finde_de_semana = Playlist('find de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_finde_de_semana)}')

print(playlist_finde_de_semana[0])


for programa in playlist_finde_de_semana:
    print(programa)


