class Viagem:
  def __init__(self):
    self.__d = 0
    self.__t = 0

  def set_distancia(self, d):
    if d >= 0: self.__d = d
    else: raise ValueError()

  def set_tempo(self, t):
    if t >= 0: self.__t = t
    else: raise ValueError()

  def get_distancia(self):
    return self.__d
    
  def get_tempo(self):
    return self.__t

  def calc_velocmed(self):
    return self.__d / self.__t

class UI:
  @staticmethod
  def main():
    x = Viagem()
    x.set_distancia(10)
    h = 1
    m = 30
    t = h + (m / 60)
    x.set_tempo(t)
    print(f'Velocidade média = {x.calc_velocmed()}')
    
UI.main() 
