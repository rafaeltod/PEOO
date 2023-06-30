class Energia:
  def __init__(self, m, a, c):
    self.__mes = 0
    self.__ano = 0
    self.__consumo = 0

    self.set_mes(m)
    self.set_ano(a)
    self.set_consumo(c)

  def set_mes(self, m):
    if 1 <= m <= 12: self.__mes = m
    else: raise ValueError()

  def set_ano(self, a):
    if 1900 <= a <= 2100: self.__ano = a
    else: raise ValueError()

  def set_consumo(self, c):
    if c >= 0: self.__consumo = c
    else: raise ValueError()

  def get_mes(self):
    return self.__mes

  def get_ano(self):
    return self.__ano

  def get_consumo(self):
    return self.__consumo

  def calc_energ(self):
    if self.__consumo <= 30:
      return 10
      
    if 31 <= self.__consumo <= 300:
      return 10 + (self.__consumo - 30)

    if self.__consumo >= 301:
      return 280 + (self.__consumo - 300) * 1.5

  def __str__(self):
    return f'Sua conta foi do mês {self.__mes}/{self.__ano} e foram consumidos {self.__consumo}'

class UI:
  @staticmethod
  class main():
    m = int(input("Digite o mês: "))
    a = int(input("Digite o ano: "))
    c = int(input("Digite o consumo em kwh: "))
    x = Energia(m, a, c)
    print(x)
    print(f'Seu consumo em reais foram dados por R$ {x.calc_energ():.2f}')