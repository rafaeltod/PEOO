import json
from datetime import datetime
from datetime import timedelta

class Agenda:
  def __init__(self, id, data, confirmado, idCliente, idServico):
    self.__id = id
    self.__data = data
    self.__confirmado = confirmado
    self.__idCliente = idCliente
    self.__idServico = idServico
  def get_id(self): return self.__id
  def get_data(self): return self.__data
  def get_confirmado(self): return self.__confirmado
  def get_idCliente(self): return self.__idCliente
  def get_idServico(self): return self.__idServico
  def set_id(self, id): self.__id = id
  def set_data(self, data): self.__data = data
  def set_confirmado(self, confirmado): self.__confirmado = confirmado
  def set_idCliente(self, idCliente): self.__idCliente = idCliente
  def set_idServico(self, idServico): self.__idServico = idServico
  def __str__(self):
    return f"{self.__id} - {self.__data} - {self.__confirmado} - {self.__idCliente} - {self.__idServico}"
  def dicionario(self):
    return {"id" : self.__id, "data" : self.__data.strftime("%d/%m/%Y %H:%M"), "confirmado" : self.__confirmado, "idCliente" : self.__idCliente, "idServico" : self.__idServico}


class NAgenda:
  __agendas = []
  @classmethod
  def inserir(cls, obj):
    NAgenda.abrir()
    id = 0
    for agenda in cls.__agendas:
      if agenda.get_id() > id: id = agenda.get_id()
    obj.set_id(id + 1)
    cls.__agendas.append(obj)
    NAgenda.salvar()
  @classmethod
  def listar(cls):
    NAgenda.abrir()    
    return cls.__agendas
  @classmethod
  def listar_id(cls, id):
    NAgenda.abrir()
    for agenda in cls.__agendas:
      if agenda.get_id() == id: return agenda
    return None
  @classmethod
  def atualizar(cls, obj):
    NAgenda.abrir()
    agenda = cls.listar_id(obj.get_id())
    agenda.set_data(obj.get_data())
    agenda.set_confirmado(obj.get_confirmado())
    NAgenda.salvar()
  @classmethod
  def excluir(cls, obj):
    NAgenda.abrir()
    agenda = cls.listar_id(obj.get_id())
    cls.__agendas.remove(agenda)    
    NAgenda.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__agendas = []
      with open("agendas.json", mode="r") as f:
        s = json.load(f)
        for agenda in s:
          a = Agenda(agenda["id"], datetime.strptime(agenda["data"], "%d/%m/%Y %H:%M"),
                     agenda["confirmado"], agenda["idCliente"], agenda["idServico"])
          cls.__agendas.append(a)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("agendas.json", mode="w") as f:
      json.dump(cls.__agendas, f, default = Agenda.dicionario)