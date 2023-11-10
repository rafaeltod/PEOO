import datetime

class Paciente:
  def __init__(self, nome, cpf, telefone, nascimento):
    self.__nome = str()
    self.__cpf = str()
    self.__telefone = str()
    self.__nascimento = str()

    self.setnome(nome)
    self.setcpf(cpf)
    self.settelefone(telefone)
    self.setnascimento(nascimento)

  def setnome(self, nome):
    if nome != "": self.__nome = nome
    else: raise ValueError()

  def setcpf(self, cpf):
    if cpf != "": self.__cpf = cpf
    else: raise ValueError()

  def settelefone(self, telefone):
    if telefone != "": self.__telefone = telefone
    else: raise ValueError()

  def setnascimento(self, nascimento):
    if nascimento != "": self.__nascimento = nascimento
    else: raise ValueError()

  def getnome(self):
    return self.__nome

  def getcpf(self):
    return self.__cpf

  def gettelefone(self):
    return self.__telefone

  def getnascimento(self):
    return self.__nascimento

  def Idade(self):
    hoje = datetime.datetime.today()
    idade = hoje - self.__nascimento
    anos = idade.days // 365
    meses = idade.days % 365 // 30
    dias = idade.days % 365 % 30
    return f'O paciente tem {anos} ano(s), {meses} mes(es) e {dias} dia(s)'

  def __str__(self):
    nascimento_txt = self.__nascimento.strftime("%d/%m/%Y")
    return f' | Paciente: {self.__nome} \n | CPF: {self.__cpf} \n | Telefone: {self.__telefone} \n | Nascimento: {nascimento_txt}'

class UI:
  @staticmethod
  def main():
    nome = input("Seu nome: ")
    cpf = input("CPF do paciente: ")
    telefone = input("Telefone: ")
    nascimento = input("Nascimento do paciente (dd/mm/yyyy): \n")
    nascimento = datetime.datetime.strptime(nascimento, "%d/%m/%Y")
    x = Paciente(nome, cpf, telefone, nascimento)
    print(x)
    print(x.Idade())

UI.main()