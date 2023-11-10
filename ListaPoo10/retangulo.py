class Retangulo:
  def __init__(self, b, h):
    self.__b = b
    self.__h = h
    if b > 0: self.__b = b
    else: raise ValueError()
    if h > 0: self.__h = h
    else: raise ValueError()
  def set_base(self, b):
    if b > 0: self.__b = b
    else: raise ValueError()
  def get_base(self):
    return self.__b
  def set_altura(self, h):
    if h > 0: self.__h = h
    else: raise ValueError()
  def get_altura(self):
    return self.__h
  def __str__(self):
      return f"Base = {self.__b}  Altura = {self.__h}"
try:
  b = int(input("Informe a base: "))
  h = int(input("Informe a altura: "))
  r = Retangulo(b, h)
  print(r)
except ValueError:
  print("Valores inválidos")