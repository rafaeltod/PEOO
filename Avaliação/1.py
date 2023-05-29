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
    n = input("Informe seu nome: ")
    p = int(input("Informe a população: "))
    a = float(input("Informe sua área: "))
    x = Pais(n, p, a)
    print(x)
    print(f'Sua Densidade é {x.calc_dens()} hab/km²')
    maior = x
    for k in range(2, 11):
      print(f"Informe nome, população e área do {k}º pais")
      n = input("Informe seu nome: ")
      p = int(input("Informe a população: "))
      a = float(input("Informe sua área: "))
      x = Pais(n, p, a)
      print(x)
      print(f'Sua Densidade é {x.calc_dens()} hab/km²')
      if (x.calc_dens() > maior.calc_dens()): maior = x
    print(f'Dados do país com maior densidade: \n {maior}')    
    print(f'E sua densidade é {maior.calc_dens()} hab/km²')    
      
UI.main()