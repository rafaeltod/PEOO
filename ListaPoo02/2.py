class Media:
  def __init__(self, s, n1, n2, n3, n4, nf):
    self.__nome = str()
    self.__n1 = int()
    self.__n2 = int()
    self.__n3 = int()
    self.__n4 = int()
    self.__nf = int()

    self.set_nome(s)
    self.set_nota1(n1)
    self.set_nota2(n2)
    self.set_nota3(n3)
    self.set_nota4(n4)
    self.set_nota_final(nf)

  def set_nome(self, s):
    if s != "": self.__nome = s
    else: raise ValueError()
      
  def set_nota1(self, n1):
    if 0 <= n1 <= 100: self.__n1 = n1
    else: raise ValueError()
      
  def set_nota2(self, n2):
    if 0 <= n2 <= 100: self.__n2 = n2
    else: raise ValueError()
      
  def set_nota3(self, n3):
    if 0 <= n3 <= 100: self.__n3 = n3
    else: raise ValueError()
      
  def set_nota4(self, n4):
    if 0 <= n4 <= 100: self.__n4 = n4
    else: raise ValueError()
      
  def set_nota_final(self, nf):
    if 0 <= nf <= 100: self.__nf = nf
    else: raise ValueError()

  def get_nome(self):
    return self.__nome
    
  def get_nota1(self):
    return self.__n1
    
  def get_nota2(self):
    return self.__n2
    
  def get_nota3(self):
    return self.__n3
    
  def get_nota4(self):
    return self.__n4
    
  def get_nota_final(self):
    return self.__nf

  def calc_medprc(self):
    return ((self.__n1 * 2) + (self.__n2 * 2) + (self.__n3 * 3) + (self.__n4 * 3)) / 10
    
  def calc_medfnl(self):
    if self.calc_medprc() < 60: 
      return ((self.calc_medprc()) + (self.__nf)) / 2
    else:
      return self.calc_medprc()

  def __str__(self):
    return f'Matéria: {self.__nome} \n - 1° Bim: {self.__n1} \n - 2° Bim: {self.__n2} \n - 3° Bim: {self.__n3} \n - 4° Bim: {self.__n4} \n - Nota Final: {self.__nf}'
      
class UI:
  @staticmethod
  def main():
    print("Digite as notas da disciplina abaixo \n")
    s = input("Nome da matéria: ")
    n1 = int(input("Nota do primeiro bimestre: "))
    n2 = int(input("Nota do segundo bimestre: "))
    n3 = int(input("Nota do terceiro bimestre: "))
    n4 = int(input("Nota do quarto bimestre: "))
    nf = int(input("Nota final: "))
    x = Media(s, n1, n2, n3, n4, nf)
    print(x)
    print(f' Matéria = {x.get_nome()}')
    print(f' Média Parcial = {x.calc_medprc()}')
    print(f' MÉDIA FINAL = {x.calc_medfnl()}')

UI.main()