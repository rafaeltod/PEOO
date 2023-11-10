import json
from datetime import datetime
from datetime import timedelta

class Compromisso:
  def __init__(self, id, assunto, local, data):
    self.__id = id
    self.__assunto = assunto
    self.__local = local
    self.__data = data
  def get_id(self): return self.__id
  def get_assunto(self): return self.__assunto
  def get_local(self): return self.__local
  def get_data(self): return self.__data
  def set_id(self, id): self.__id = id
  def set_assunto(self, assunto): self.__assunto = assunto
  def set_local(self, local): self.__local = local
  def set_data(self, data): self.__data = data
  def __str__(self):
    return f"{self.__id} - {self.__assunto} - {self.__local} - {self.__data}"
  def dicionario(self):
    return {"id" : self.__id, "assunto" : self.__assunto, "local" : self.__local, "data" : self.__data.strftime("%d/%m/%Y %H:%M")}

class NCompromisso:
  __compromissos = []        
  @classmethod
  def inserir(cls, obj):
    NCompromisso.abrir()
    id = 0 
    for compromisso in cls.__compromissos:
      if compromisso.get_id() > id: id = compromisso.get_id()
    obj.set_id(id + 1)
    cls.__compromissos.append(obj)  
    NCompromisso.salvar()
  @classmethod
  def listar(cls):
    NCompromisso.abrir()    
    return cls.__compromissos   
  @classmethod
  def listar_id(cls, id):
    NCompromisso.abrir()
    for compromisso in cls.__compromissos:
      if compromisso.get_id() == id: return compromisso
    return None
  @classmethod
  def atualizar(cls, obj):
    NCompromisso.abrir()
    compromisso = cls.listar_id(obj.get_id())
    compromisso.set_assunto(obj.get_assunto())
    compromisso.set_local(obj.get_local())
    compromisso.set_data(obj.get_data())
    NCompromisso.salvar()
  @classmethod
  def excluir(cls, obj):
    NCompromisso.abrir()
    compromisso = cls.listar_id(obj.get_id())
    cls.__compromissos.remove(compromisso)    
    NCompromisso.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__compromissos = []
      with open("compromissos.json", mode="r") as f:
        s = json.load(f)
        for compromisso in s:
          c = Compromisso(compromisso["id"], compromisso["assunto"],
                     compromisso["local"], datetime.strptime(compromisso["data"], "%d/%m/%Y %H:%M"))
          cls.__compromissos.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("compromissos.json", mode="w") as f:
      json.dump(cls.__compromissos, f, default = Compromisso.dicionario)
  @classmethod
  def Comps_do_Mes(cls):
    NCompromisso.abrir()
    cls.__compsdomes = []
    hoje = datetime.now()
    mesatual = hoje.month
    anoatual = hoje.year
    for compromisso in cls.__compromissos:
      if compromisso.get_data().month == mesatual and compromisso.get_data().year == anoatual:
        cls.__compsdomes.append(compromisso)
    return cls.__compsdomes

class UI:
  @classmethod
  def Main(cls):
    op = 99
    while(op != 0):
      op = UI.Menu()
      if op == 1: UI.CompromissoInserir()
      if op == 2: UI.CompromissoListar()
      if op == 3: UI.CompromissoAtualizar()
      if op == 4: UI.CompromissoExcluir()
      if op == 5: UI.ListarCompsDoMes()
        
  @classmethod
  def Menu(cls):
    print("1 - Inserir Compromisso\n2 - Listar Compromissos\n3 - Atualizar Compromissos\n4 - Excluir Compromisso\n5 - Listar Compromissos do Mês\n0 - Sair")
    return int(input())
  @classmethod
  def CompromissoInserir(cls):
    assunto = input("Assunto: ")
    local = input("Local: ")
    data = datetime.strptime(input("Data: "), "%d/%m/%Y %H:%M")
    compromisso = Compromisso(0, assunto, local, data)
    NCompromisso.inserir(compromisso)
  @classmethod
  def CompromissoListar(cls):
    for compromisso in NCompromisso.listar():
      print(compromisso)
  @classmethod
  def CompromissoAtualizar(cls):
    UI.CompromissoListar()
    id = int(input("Id do compromisso a ser atualizado: "))
    assunto = input("Novo assunto: ")
    local = input("Novo local: ")
    data = datetime.strptime(input("Data: "), "%d/%m/%Y %H:%M")
    compromisso = Compromisso(id, assunto, local, data)
    NCompromisso.atualizar(compromisso)    
  @classmethod
  def CompromissoExcluir(cls):
    UI.CompromissoListar()
    id = int(input("Id do compromisso a ser excluído: "))
    compromisso = Compromisso(id, "", "", "")
    NCompromisso.excluir(compromisso)
  @classmethod
  def ListarCompsDoMes(cls):
    for compromisso in NCompromisso.Comps_do_Mes():
      print(compromisso)

UI.Main()