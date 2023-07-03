class Cliente:
  def __init__(self, nome, cpf, limite):
    self.__nome = nome
    self.__cpf = cpf
    self.__limite = limite
    self.__socio = None
    
  def setsocio(self, socio):
    if self.__socio == None:
      self.__socio = socio
      
  def getlimite(self):
    if self.__socio != None:
      return self.__limite + self.__socio.__limite
    return self.__limite
    
  def __str__(self):
    return f'{self.__nome} - {self.__cpf} | Limite de {self.__limite}'

class Empresa:
  def __init__(self):
    self.__clientes = []
    
  def inserir(self, cliente):
    self.__clientes.append(cliente)
    
  def listar(self):
    lista = ''
    for c in self.__clientes:
      lista += f'{str(c)}\n'
    return lista
    
  def getclientes(self):
    return self.__clientes

class UI:
  @staticmethod
  def menu():
    print("1 - Inserir, 2 - Listar, 3 - Criar sociedade, 4 - Checar limite, 0 - Fim \n")
    return int(input())
  
  @staticmethod
  def main():
    op = 10
    x = Empresa()
    while op != 0:
      op = UI.menu()
      if op == 1:
        cliente = Cliente(input("Insira o nome do cliente:\n"), int(input("Insira CPF do cliente:\n")), int(input("Limite do cartão:\n")))
        x.inserir(cliente)
      if op == 2:
        print(x.listar())
      if op == 3:
        socio1 = x.getclientes()[int(input("Número do cliente 1:\n"))-1]
        socio2 = x.getclientes()[int(input("Número do cliente 2:\n"))-1]
        socio1.setsocio(socio2)
        socio2.setsocio(socio1)
      if op == 4:
        cliente = x.getclientes()[int(input("Qual cliente deseja checar? "))-1]
        print(cliente.getlimite())

UI.main()