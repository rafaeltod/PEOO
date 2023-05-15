class Media:
  def __init__(self):
    self.nome = ""
    self.n1 = 0
    self.n2 = 0
    self.n3 = 0
    self.n4 = 0
    self.pf = 0
  def calc_medprc(self):
    return ((self.n1 * 2) + (self.n2 * 2) + (self.n3 * 3) + (self.n4 * 3)) / 10
  def calc_medfnl(self):
    if self.calc_medprc() < 60: 
      return ((self.calc_medprc()) + (self.pf)) / 2
    else:
      return self.calc_medprc()
x = Media()
x.nome = "PEOO"
x.n1 = 60
x.n2 = 60
x.n3 = 60
x.n4 = 60
x.pf = 0
print(f' Matéria = {x.nome}, Média Parcial = {x.calc_medprc()}')
print(f' MÉDIA FINAL = {x.calc_medfnl()}')