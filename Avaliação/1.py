class Pais():
    def __init__(self, n, p, a):
        self.__nome = ''
        self.__peop = 0
        self.__area = 0

        self.set_nome(n)
        self.set_peop(p)
        self.set_area(a)

    def set_nome(self, n):
        if n != "":
            self.__nome = n
        else:
            raise ValueError()

    def set_peop(self, p):
        if p >= 0:
            self.__peop = p
        else:
            raise ValueError()

    def set_area(self, a):
        if a >= 0:
            self.__area = a
        else:
            raise ValueError()

    def get_nome(self):
        return self.__nome

    def get_peop(self):
        return self.__peop

    def get_area(self):
        return self.__area

    def calc_dens(self):
        return self.__peop / self.__area

    def __str__(self):
        return f'Pais: {self.__nome} - População: {self.__peop} habitantes - Área: {self.__area} km²'

class UI:
  @staticmethod
  def main():
    print("Informe nome, população e área do 1º pais")
    x = Pais(input(), int(input()), float(input()))
    maior = x
    for k in range(2, 11):
      print(f"Informe nome, população e área do {k}º pais")
      x = Pais(input(), int(input()), float(input()))
      if (x.calc_dens() > maior.calc_dens()): maior = x
    print(maior)    
    print(maior.calc_dens())    
      
UI.main()