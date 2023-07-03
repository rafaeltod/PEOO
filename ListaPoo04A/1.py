import random

class Bingo:
  def __init__(self):
    self.__numBolas = int()
    self.__sorteados = []

  def Iniciar(self, numBolas):
    if numBolas > 0: self.__numBolas = numBolas
    else: raise ValueError("Número inválido")

  def Proximo(self):
    if len(self.__sorteados) == self.__numBolas:
      return -1  
    else:
      bola_sorteada = random.randint(1, self.__numBolas)
      while bola_sorteada in self.__sorteados:
        bola_sorteada = random.randint(1, self.__numBolas)
      self.__sorteados.append(bola_sorteada)
      return bola_sorteada

  def Sorteados(self):
    return self.__sorteados
    
class UI:
  @staticmethod
  def menu():
    print("0 - Fim, 1 - Bingo, 2 - Sortear, 3 - Sorteados")
    return int(input())

  @staticmethod
  def main():
    op = 10
    x = Bingo()
    while op != 0:
      op = UI.menu()
      if op == 1:
        bolas = int(input("Quantidade de bolas: "))
        x.Iniciar(bolas)
      if op == 2:
        print(f'Bola sorteada: {x.Proximo()}')
      if op == 3:
        print(f'Bolas já sorteadas: {x.Sorteados()} ')

UI.main()