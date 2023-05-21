class Circulo:
  def __init__(self):
    self.__r = 0
    
  def set_raio(self, v):
    if v >= 0: self.__r = v
    else: raise ValueError()
      
  def get_raio(self):
    return self.__r
    
  def calc_area(self):
    return 3.14 * (self.__r ** 2)
    
  def calc_circuferencia(self):
    return 2 * 3.14 * self.__r

class UI:
  @staticmethod
  def main():
    x = Circulo()
    x.set_raio(8)
    print(x.calc_area())
    print(x.calc_circuferencia())
    
UI.main()