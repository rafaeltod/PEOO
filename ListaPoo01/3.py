class Viagem:
  def __init__(self):
    self.d = 0
    self.h = 0
    self.m = 0
  def calc_veloc(self):
    return self.d/((self.h*60 + self.m)/60)

x = Viagem()
x.d = 120
x.h = 1
x.m = 30
print(f'Velocidade média = {x.calc_veloc()}')