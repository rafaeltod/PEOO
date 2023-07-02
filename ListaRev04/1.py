class Jogador:
  def __init__(self, nome, camisa, gols):
    self.__nome = str()
    self.__camisa = int()
    self.__gols = int()

    self.setnome(nome)
    self.setcamisa(camisa)
    self.setgols(gols)

  def setnome(self, nome):
    if nome != "": self.__nome = nome
    else: raise ValueError()

  def setcamisa(self, camisa):
    if 0 <= camisa <= 100: self.__camisa = camisa
    else: raise ValueError()

  def setgols(self, gols):
    if gols >= 0: self.__gols = gols
    else: raise ValueError()

  def getnome(self):
    return self.__nome

  def getcamisa(self):
    return self.__camisa

  def getgols(self):
    return self.__gols

  def __str__(self):
    return f'Nome: {self.__nome} | Camisa: Número {self.__camisa} | Gols = {self.__gols}'

class Time:
  def __init__(self, nome, estado):
    self.__nome = str()
    self.__estado = str()
    self.__jogadores = []

    self.setnome(nome)
    self.setestado(estado)

  def setnome(self, nome):
    if nome != "": self.__nome = nome
    else: raise ValueError()

  def setestado(self, estado):
    if estado != "": self.__estado = estado
    else: raise ValueError()

  def inserir(self, jogador):
    self.__jogadores.append(jogador)

  def listar(self):
    listados = str()
    for j in self.__jogadores:
      listados += f'{str(j)}\n'
    return listados

  def artilheiro(self):
    if len(self.__jogadores) == 0: return None
    artilheiro = self.__jogadores[0]
    for j in self.__jogadores:
      if j.getgols() > artilheiro.getgols():
        artilheiro = j
    return artilheiro

  def __str__(self):
    return f'Time: {self.__nome} | Estado: {self.__estado}'

class UI:
  @staticmethod
  def menu():
    print("0-Fim, 1-Inserir, 2-Listar, 3-Artilheiro")
    return int(input())

  @staticmethod
  def main():
    op = 10
    nometime = input("Nome do time: ")
    estado = input("Estado do time: ")
    x = Time(nometime, estado)
    while op != 0:
      op = UI.menu()
      if op == 1:
        nome = input("Nome do jogador: ")
        camisa = int(input("Camisa: "))
        gols = int(input("Gols: "))
        j = Jogador(nome, camisa, gols)
        x.inserir(j)
      if op == 2:
        print(x.listar())
      if op == 3:
        print(x.artilheiro())

UI.main()