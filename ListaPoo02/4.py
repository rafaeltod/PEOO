class Cinema:
  def __init__(self):
    self.__dia = ''
    self.__horario = 0

  def set_dia(self, d):
    ld = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    if d in ld: self.__dia = d
    else: raise ValueError()

  def set_horario(self, h):
    if 0 <= h <= 23: self.__horario = h
    else: raise ValueError()

  def get_dia(self):
    return self.__dia

  def get_horario(self):
    return self.__horario
    
  def calc_valorinteiro(self):
    valor1 = ['Segunda', 'Terça', 'Quinta']
    valor2 = ['Sexta', 'Sábado', 'Domingo']
    if self.__dia in valor1:
      valor = 16
      if self.__horario >= 17:
        valor *= 1.5
    elif self.__dia == 'Quarta':
      valor = 8
    elif self.__dia in valor2:
      valor = 20
      if self.__horario >= 17:
        valor *= 1.5
    return valor
    
  def calc_valormeia(self):
    valor1 = ['Segunda', 'Terça', 'Quinta']
    valor2 = ['Sexta', 'Sábado', 'Domingo']
    if self.__dia in valor1:
      valor = 8
      if self.__horario >= 17:
        valor *= 1.5
    elif self.__dia == 'Quarta':
      valor = 8
    elif self.__dia in valor2:
      valor = 10
      if self.__horario >= 17:
        valor *= 1.5
    return valor

class UI:
  @staticmethod
  def main():
    x = Cinema()
    x.set_dia('Terça')
    x.set_horario(18)
    print(f'O valor inteiro vai sair por {x.calc_valorinteiro()}')
    print(f'O valor da meia vai sair por {x.calc_valormeia()}')

UI.main()