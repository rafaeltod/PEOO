class Esporte:
  def __init__(self, nome, horarios, mensalidade):
    self.__nome = str()
    self.__horarios = str()
    self.__mensalidade = float()

    self.setnome(nome)
    self.sethorarios(horarios)
    self.setmensalidade(mensalidade)

  def setnome(self, nome):
    if nome != "": self.__nome = nome
    else: raise ValueError()

  def sethorarios(self, horarios):
    if horarios != "": self.__horarios = horarios
    else: raise ValueError()

  def setmensalidade(self, mensalidade):
    if mensalidade > 0: self.__mensalidade = mensalidade
    else: raise ValueError()

  def getnome(self):
    return self.__nome

  def gethorarios(self):
    return self.__horarios

  def getmensalidade(self):
    return self.__mensalidade

  def __str__(self):
    return f'\n Modalidade: {self.__nome} | Horário: {self.__horarios} | Mensalidade: {self.__mensalidade} reais \n'

class Academia:
  def __init__(self, nome, endereco):
    self.__nome = nome
    self.__endereco = endereco
    self.__esportes = []

    self.setnome(nome)
    self.setendereco(endereco)

  def setnome(self, nome):
    if nome != "": set__nome = nome
    else: raise ValueError()

  def setendereco(self, endereco):
    if endereco != "": set_endereco = endereco
    else: raise ValueError()

  def inserir(self, esporte):
    self.__esportes.append(esporte)

  def listar(self):
    return self.__esportes

  def media_mensalidade(self):
    soma = 0
    for esporte in self.__esportes:
      soma += esporte.getmensalidade()
    return soma / len(self.__esportes)

  def __str__(self):
    return f'--- Academia: {self.__nome} | Endereço: {self.__endereco} ---'

class UI:
  @staticmethod
  def menu():
    print("0 - Fim, 1 - Inserir, 2 - Listar, 3 - Média da Mensalidade")
    return int(input())

  @staticmethod
  def main():
    op = 10
    nomeacad = input("Nome da Academia: ")
    endereco = input("Endereco da Academia: ")
    x = Academia(nomeacad, endereco)
    while op != 0:
      op = UI.menu()
      if op == 1:
        nome = input("Modalidade: ")
        horarios = str(input("Horário: "))
        mensalidade = int(input("Mensalidade: "))
        p = Esporte(nome, horarios, mensalidade)
        x.inserir(p)
      if op == 2:
        print(x)
        print(*x.listar())
      if op == 3:
        print(x.media_mensalidade())

UI.main()