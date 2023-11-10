class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone

  def set_nome(self, nome):
    if nome != '': self.__nome = nome
    else: raise ValueError()

  def set_email(self, email):
    if email != '': self.__email = email
    else: raise ValueError()

  def set_fone(self, fone):
    if fone != '': self.__fone = fone
    else: raise ValueError()

  def get_id(self):
    return self.__id

  def get_nome(self):
    return self.__nome

  def get_email(self):
    return self.__email

  def get_fone(self):
    return self.__fone

  def __str__(self):
    return f"ID: {self.__id} | Cliente: {self.__nome} | E-mail: {self.__email} | Telefone: {self.__fone}"

class NCliente:
  def __init__(self):
    self.__clientes = []
    
  def Inserir(self, cliente):   
    self.__clientes.append(cliente)
    
  def Listar(self):
    return self.__clientes

  def Listar_Id(self, id):
    for cliente in self.__clientes:
      if cliente.get_id() == id:
        return cliente
    
  def Atualizar(self, cliente):
    for obj in self.__clientes:
      if obj.get_id() == cliente.get_id():
        obj.set_nome(cliente.get_nome())
        obj.set_email(cliente.get_email())
        obj.set_fone(cliente.get_fone())
        
  def Excluir(self, cliente):
    self.__clientes.remove(cliente)

class UI:
  @staticmethod
  def menu():
    print("0 - Fim, 1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir")
    return int(input())

  @staticmethod
  def main():
    op = 10
    x = NCliente()
    while op != 0:
      op = UI.menu()
      if op == 1:
        id = int(input("Id: "))
        nome = input("Cliente: ")
        email = input("E-mail: ")
        fone = input("Telefone: ")
        c = Cliente(id, nome, email, fone)
        x.Inserir(c)
      if op == 2:
        print(*x.Listar())
      if op == 3:
        id = int(input("Id: "))
        nome = input("Cliente: ")
        email = input("E-mail: ")
        fone = input("Telefone: ")
        novo = Cliente(id, nome, email, fone)
        print(x.Atualizar(novo))
      if op == 4:
        id = int(input("Id: "))
        clienteExcluido = x.Listar_Id(id)
        print(x.Excluir(clienteExcluido))

UI.main()