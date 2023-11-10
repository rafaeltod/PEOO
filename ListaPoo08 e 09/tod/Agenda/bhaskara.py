class Bhaskara:
  def __init__(self, a, b, c):
    self.__a = 1
    self.__b = 0
    self.__c = 0
    self.__px = []
    self.__py = []

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

  def set_px(self, px):
    self.__px = px

  def set_py(self, py):
    self.__py = py

  def get_a(self):
    return self.__a

  def get_b(self):
    return self.__b

  def get_c(self):
    return self.__c

  def get_px(self):
    return self.__px

  def get_py(self):
    return self.__py

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

  def calc_p(self):
        d = self.Raiz1() - self.Raiz2()
        xmin = self.Raiz1() - d
        xmax = self.Raiz2() + d
        e = (xmax-xmin)/100
        x = xmin
        while x<= (xmax + e):
            self.__px.append(x)
            self.__py.append(self.__a * x ** 2 + self.__b * x + self.__c)
            x += e

  def __str__(self):
    return f'Equação do 2° Grau: {self.__a}x² + {self.__b}x + {self.__c} = 0'