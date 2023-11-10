import datetime

class Musica:
  def __init__(self, titulo, artista, album, dataInclusao, duracao):
    self.__titulo = titulo
    self.__artista = artista
    self.__album = album
    self.__dataInclusao = dataInclusao
    self.__duracao = duracao

  def getduracao(self):
    return self.__duracao

  def __str__(self):
    return f' \n Música: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album} | Data de Inclusão: {self.__dataInclusao} | Duração: {self.__duracao} \n '

class PlayList:
  def __init__(self, nome, descricao):
    self.__nome = nome
    self.__descricao = descricao
    self.__musicas = []

  def inserir(self, musica):
    self.__musicas.append(musica)

  def listar(self):
    return self.__musicas

  def tempo_total(self):
    duracao = datetime.timedelta()
    for musica in self.__musicas:
      duracao += musica.getduracao()
    return duracao

  def __str__(self):
    return f'Nome da Playlist: {self.__nome}, Descrição: {self.__descricao}'

class UI:
  @staticmethod
  def menu():
    print(" 0 - Fim, 1 - Inserir, 2 - Listar, 3 - Duração ")
    return int(input())

  @staticmethod
  def main():
    op = 10
    nome = input("Nome da Playlist: ")
    descricao = input("Descrição da Playlist: ")
    playlist = PlayList(nome, descricao)
    while op != 0:
      op = UI.menu()
      if op == 1:
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")
        mm, ss = map(int, input("Insira a duração (mm:ss):\n").split(":"))
        duracao = datetime.timedelta(minutes = mm, seconds = ss)
        dataInclusao = datetime.datetime.today()
        musica = Musica(titulo, artista, album, dataInclusao, duracao)
        playlist.inserir(musica)
      if op == 2:
        print(playlist)
        print(*playlist.listar())
      if op == 3:
        print(f' \n O Tempo de duração da Playlist é: {playlist.tempo_total()} \n ')

UI.main()