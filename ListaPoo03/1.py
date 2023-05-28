class Retangulo:
  def __init__(self, b, h):
    self.__b = 0
    self.__h = 0

    self.set_base(b)
    self.set_altura(h)

  def set_base(self, b):
    if b >= 0: self.__b = b
    else: raise ValueError()

  def set_altura(self, h):
    if h >= 0: self.__h = h
    else: raise ValueError()

  def get_base(self):
    return self.__b

  def get_altura(self):
    return self.__h

  def calc_area(self):
    return self.__b * self.__h

  def calc_diag(self):
    return ((self.__b ** 2) + (self.__h ** 2)) ** 0.5

  def __str__(self):
    return f'Base = {self.__b} m - Altura = {self.__h} m'

class UI:
  @staticmethod
  def main():
    b = float(input("Digite a base do retângulo: "))
    h = float(input("Digite a altura do retângulo: "))
    x = Retangulo(b, h)
    print(x)
    print(f'Sua Área é {x.calc_area()} m²')
    print(f'Sua Diagonal é {x.calc_diag()} m²')

UI.main()