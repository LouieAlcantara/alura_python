class Programa:
    def __init__ (self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    @property
    def likes (self):
        return self._likes
    def dar_like(self):
        self._likes += 1
    @property
    def nome (self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome


class Filme(Programa):
     def __init__ (self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
class Serie(Programa):
    def __init__ (self, nome, ano, temporada):
        super().__init__ (nome, ano)
        self.temporada = temporada

class Playlist():
    def __init__(self,nome, programas):
        self.nome = nome
        self.programas = programas
    def __getitem__ (self, item):
        return self.programas[item]

batman = Filme('batman', 2015, 300)

batman.dar_like()
batman.dar_like()

lista = [batman]

for programa in lista:
    print(f'Nome: {programa.nome} - Likes: {programa.likes}')