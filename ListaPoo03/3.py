class Bhaskara:
  def __init__(self, a, b, c):
    self.__a = 1
    self.__b = 0
    self.__c = 0

    self.set_a(a)
    self.set_b(b)
    self.set_c(c)

  def set_a(self, a):
    if a != 0:
      self.__a = a
    else:
      raise ValueError()

  def set_b(self, b):
    self.__b = b

  def set_c(self, c):
    self.__c = c

  def get_a(self):
    return self.__a

  def get_b(self):
    return self.__b

  def get_c(self):
    return self.__c

  def delta(self):
    self.__delta = (self.__b ** 2) - (4 * self.__a * self.__c)
    return f'Delta = {self.__delta}'
  
  def raizesreais(self):
    if self.__delta >= 0:
      return True
    else:
      return False

  def Raiz1(self):
    return (-self.__b + (self.__delta)**0.5) / (2 * self.__a)

  def Raiz2(self):
    return (-self.__b - (self.__delta)**0.5) / (2 * self.__a)

  def __str__(self):
    return f'Equação do 2° Grau: {self.__a}x² + {self.__b}x + {self.__c} = 0'

class UI:
  @staticmethod
  def main():
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    x = Bhaskara(a, b, c)
    print(x)
    print(x.delta())
    print(x.raizesreais())
    print(f'A primeira Raiz vai ser {x.Raiz1()} e a segunda Raiz vai ser {x.Raiz2()}')

UI.main()