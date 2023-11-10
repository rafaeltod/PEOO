class Local:
  def __init__(self, id, nome, endereco, fone):
    self.__id = id
    self.__nome = nome
    self.__endereco = endereco
    self.__fone = fone

  def set_nome(self, nome):
    if nome != '': self.__nome = nome
    else: raise ValueError()

  def set_endereco(self, endereco):
    if endereco != '': self.__endereco = endereco
    else: raise ValueError()

  def set_fone(self, fone):
    if fone != '': self.__fone = fone
    else: raise ValueError()

  def get_id(self):
    return self.__id

  def get_nome(self):
    return self.__nome

  def get_endereco(self):
    return self.__endereco

  def get_fone(self):
    return self.__fone

  def __str__(self):
    return f"ID: {self.__id} | Local: {self.__nome} | Endereço: {self.__endereco} | Telefone: {self.__fone}"

class Evento:
  def __init__(self, id, id_local, nome, data, valor):
    self.__id = id
    self.__id_local = id_local
    self.__nome = nome
    self.__data_hora = data
    self.__valor_ingresso = valor
  def __str__(self):
    return f"{self.__id} {self.__nome} {self.__data} {self.__valor}"

class NLocal: # banco de dados de locais - CRUD
  def __init__(self):
    self.locais = []
  def inserir(self, local):   # Create
    self.locais.append(local)
  def listar(self):           # Read
    return self.locais
  def atualizar(self, local): # Update
    for obj in self.locais:
      if obj.get_id() == local.get_id():
        obj.set_nome(local.get_nome())
        obj.set_endereco(local.get_endereco())
        obj.set_fone(local.get_fone())
  def excluir(self, local):   # Delete
    self.locais.remove(local)
         
a = Local(1, "Midway", "Antonio Basilio", "88888888")
b = Local(2, "IFRN", "Salgado Filho", "00008888")

x = NLocal()
x.inserir(a) # Create
x.inserir(b) # Create

for local in x.listar(): print(local) # Read
  
c = Local(2, "Mojo Dojo Casa House", "Barbielandia", "0800 575 0780")
x.atualizar(c) # Update
x.excluir(a)   # Delete

for local in x.listar(): print(local)