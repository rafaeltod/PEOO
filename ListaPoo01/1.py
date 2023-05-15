class Circulo:
  def __init__(self):
    self.r = 0
  def calc_area(self):
    return 3.14 * (self.r ** 2)
  def calc_circuferencia(self):
    return 2 * 3.14 * self.r
x = Circulo()
x.r = 8
print(x.calc_area())
print(x.calc_circuferencia())