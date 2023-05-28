class Frete():
  def __init__(self, d, p):
    self.__distancia = 0
    self.__peso = 0

    self.set_distancia(d)
    self.set_peso(p)

  def set_distancia(self, d):
    if d >= 0: self.__distancia = d
    else: raise ValueError()
      
  def set_peso(self, p):
    if p >= 0: self.__peso = p
    else: raise ValueError()

  def get_distancia(self):
    return self.__distancia

  def get_peso(self):
    return self.__peso

  def calc_frete(self):
    return self.__distancia * self.__peso * 0.01

  def __str__(self):
    return f'Distancia = {self.__distancia} km - Peso = {self.__peso} kg'

class UI:
  @staticmethod
  def main():
    d = float(input("Digite a distância de envio: "))
    p = float(input("Digite o peso do produto: "))
    x = Frete(d, p)
    print(x)
    print(f'Seu Frete é R${x.calc_frete():.2f}')

UI.main()