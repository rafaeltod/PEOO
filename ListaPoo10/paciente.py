from datetime import datetime

class Paciente:
  def __init__(self, nome, cpf, telefone, nascimento):
    self.__nome = nome
    self.__cpf = cpf
    self.__telefone = telefone
    self.__nascimento = nascimento
    if nome != "": self.__nome = nome
    else: raise IndexError()
    if cpf != "": self.__cpf = cpf
    else: raise IndexError()
    if telefone != "": self.__telefone = telefone
    else: raise IndexError()
    if nascimento.date() < datetime.today().date(): self.__nascimento = nascimento
    else: raise ValueError()

    self.set_nome(nome)
    self.set_cpf(cpf)
    self.set_telefone(telefone)
    self.set_nascimento(nascimento)
      
  def set_nome(self, n):
    if n != "": self.__nome = n
    else: raise IndexError()
  def get_nome(self):
    return self.__nome
  def set_cpf(self, c):
    if c != "": self.__cpf = c
    else: raise IndexError()
  def get_cpf(self):
    return self.__cpf
  def set_telefone(self, t):
    if t != "": self.__telefone = t
    else: raise IndexError()
  def get_telefone(self):
    return self.__telefone
  def set_nascimento(self, d):
    if d.date() < datetime.today().date(): self.__nascimento = d
    else: raise ValueError()
  def __str__(self):
      return f"Nome do paciente: {self.__nome} \n CPF do paciente: {self.__cpf} \n Telefone do paciente: {self.__telefone} \n Nascimento do paciente: {self.__nascimento}"
    
try:
  nome = input("Informe o nome do paciente: ")
  cpf = input("Informe o cpf do paciente: ")
  telefone = input("Informe o telefone do paciente: ")
  nascimento = input("Informe o nascimento do paciente (dd/mm/yyyy): ")
  nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
  p = Paciente(nome, cpf, telefone, nascimento)
  print(p)
except ValueError:
  print("Valor inválido")