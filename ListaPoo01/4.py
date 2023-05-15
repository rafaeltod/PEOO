class Cinema:
  def __init__(self):
    self.dia = ' '
    self.horario = 0
  def calc_valorinteiro(self):
    valor1 = ['Segunda', 'Terça', 'Quinta']
    valor2 = ['Sexta', 'Sábado', 'Domingo']
    if self.dia in valor1:
      valor = 16
      if self.horario >= 17:
        valor *= 1.5
    elif self.dia == 'Quarta':
      valor = 8
    elif self.dia in valor2:
      valor = 20
      if self.horario >= 17:
        valor *= 1.5
    return valor    
  def calc_valormeia(self):
    valor1 = ['Segunda', 'Terça', 'Quinta']
    valor2 = ['Sexta', 'Sábado', 'Domingo']
    if self.dia in valor1:
      valor = 8
      if self.horario >= 17:
        valor *= 1.5
    elif self.dia == 'Quarta':
      valor = 8
    elif self.dia in valor2:
      valor = 10
      if self.horario >= 17:
        valor *= 1.5
    return valor

x = Cinema()
x.dia = 'Terça'
x.horario = 18
print(f'O valor inteiro vai sair por {x.calc_valorinteiro()}')
print(f'O valor da meia vai sair por {x.calc_valormeia()}')