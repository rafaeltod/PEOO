class Media:
  def __init__(self):
    self.__nome = str()
    self.__n1 = int()
    self.__n2 = int()
    self.__n3 = int()
    self.__n4 = int()
    self.__nf = int()

  def set_nome(self, s):
    if s != "": self.__nome = s
    else: raise ValueError()
      
  def set_nota1(self, n):
    if 0 <= n <= 100: self.__n1 = n
    else: raise ValueError()
      
  def set_nota2(self, n):
    if 0 <= n <= 100: self.__n2 = n
    else: raise ValueError()
      
  def set_nota3(self, n):
    if 0 <= n <= 100: self.__n3 = n
    else: raise ValueError()
      
  def set_nota4(self, n):
    if 0 <= n <= 100: self.__n4 = n
    else: raise ValueError()
      
  def set_nota_final(self, n):
    if 0 <= n <= 100: self.__nf = n
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
      return ((self.calc_medprc()) + (self.pf)) / 2
    else:
      return self.calc_medprc()
      
class UI:
  @staticmethod
  def main():
    x = Media()
    x.set_nome("PEOO")
    x.set_nota1(60)
    x.set_nota2(60)
    x.set_nota3(60)
    x.set_nota4(60)
    x.set_nota_final(0)
    print(f' Matéria = {x.get_nome()} ')
    print(f' Média Parcial = {x.calc_medprc()} ')
    print(f' MÉDIA FINAL = {x.calc_medfnl()} ')

UI.main()