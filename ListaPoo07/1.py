import json
from datetime import datetime
from datetime import timedelta

class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_fone(self): return self.__fone
  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_email(self, email): self.__email = email
  def set_fone(self, fone): self.__fone = fone
  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class NCliente:
  __clientes = []        
  @classmethod
  def inserir(cls, obj):
    NCliente.abrir()
    id = 0 
    for cliente in cls.__clientes:
      if cliente.get_id() > id: id = cliente.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)  
    NCliente.salvar()
  @classmethod
  def listar(cls):
    NCliente.abrir()    
    return cls.__clientes   
  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()
    for cliente in cls.__clientes:
      if cliente.get_id() == id: return cliente
    return None
  @classmethod
  def atualizar(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cliente.set_nome(obj.get_nome())
    cliente.set_email(obj.get_email())
    cliente.set_fone(obj.get_fone())
    NCliente.salvar()
  @classmethod
  def excluir(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cls.__clientes.remove(cliente)    
    NCliente.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__clientes = []
      with open("clientes.json", mode="r") as f:
        s = json.load(f)
        for cliente in s:
          c = Cliente(cliente["_Cliente__id"], cliente["_Cliente__nome"],
                     cliente["_Cliente__email"], cliente["_Cliente__fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as f:
      json.dump(cls.__clientes, f, default=vars)

class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.__id = id
    self.__descricao = descricao
    self.__valor = valor
    self.__duracao = duracao
  def get_id(self): return self.__id
  def get_descricao(self): return self.__descricao
  def get_valor(self): return self.__valor
  def get_duracao(self): return self.__duracao
  def set_id(self, id): self.__id = id
  def set_descricao(self, descricao): self.__descricao = descricao
  def set_valor(self, valor): self.__valor = valor
  def set_duracao(self, duracao): self.__duracao = duracao
  def __str__(self):
    return f"{self.__id} - {self.__descricao} - {self.__valor} - {self.__duracao}"

class NServico:
  __servicos = []
  @classmethod
  def inserir(cls, obj):
    NServico.abrir()
    id = 0
    for servico in cls.__servicos:
      if servico.get_id() > id: id = servico.get_id()
    obj.set_id(id + 1)
    cls.__servicos.append(obj)
    NServico.salvar()
  @classmethod
  def listar(cls):
    NServico.abrir()    
    return cls.__servicos
  @classmethod
  def listar_id(cls, id):
    NServico.abrir()
    for servico in cls.__servicos:
      if servico.get_id() == id: return servico
    return None
  @classmethod
  def atualizar(cls, obj):
    NServico.abrir()
    servico = cls.listar_id(obj.get_id())
    servico.set_descricao(obj.get_descricao())
    servico.set_valor(obj.get_valor())
    servico.set_duracao(obj.get_duracao())
    NServico.salvar()
  @classmethod
  def excluir(cls, obj):
    NServico.abrir()
    servico = cls.listar_id(obj.get_id())
    cls.__servicos.remove(servico)    
    NServico.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__servicos = []
      with open("servicos.json", mode="r") as f:
        s = json.load(f)
        for servico in s:
          svc = Servico(servico["_Servico__id"], servico["_Servico__descricao"],
                     servico["_Servico__valor"], servico["_Servico__duracao"])
          cls.__servicos.append(svc)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("servicos.json", mode="w") as f:
      json.dump(cls.__servicos, f, default=vars)

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
  
      
class UI:
  @classmethod
  def Main(cls):
    op = 99
    while(op != 0):
      op = UI.Menu()
      if op == 1: UI.ClienteInserir()
      if op == 2: UI.ClienteListar()
      if op == 3: UI.ClienteAtualizar()
      if op == 4: UI.ClienteExcluir()
      if op == 5: UI.ServicoInserir()
      if op == 6: UI.ServicoListar()
      if op == 7: UI.ServicoAtualizar()
      if op == 8: UI.ServicoExcluir()
      if op == 9: UI.AgendaInserir()
      if op == 10: UI.AgendaListar()
      if op == 11: UI.AgendaAtualizar()
      if op == 12: UI.AgendaExcluir()
      if op == 13: UI.AbrirAgenda()
        
  @classmethod
  def Menu(cls):
    print("1 - Inserir Cliente\n2 - Listar Clientes\n3 - Atualizar Clientes\n4 - Excluir Cliente\n5 - Inserir Serviço\n6 - Listar Serviço\n7 - Atualizar Serviço\n8 - Excluir Serviço\n9 - Inserir Agenda\n10 - Listar Agenda\n11 - Atualizar Agenda\n12 - Excluir Agenda\n13 - Abrir Agenda\n0 - Sair")
    return int(input())
  @classmethod
  def ClienteInserir(cls):
    nome = input("Nome: ")
    email = input("E-mail: ")
    fone = input("Telefone: ")
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)
  @classmethod
  def ClienteListar(cls):
    for cliente in NCliente.listar():
      print(cliente)
  @classmethod
  def ClienteAtualizar(cls):
    UI.ClienteListar()
    id = int(input("Id do cliente a ser atualizado: "))
    nome = input("Novo nome: ")
    email = input("Novo e-mail: ")
    fone = input("Novo telefone: ")
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)    
  @classmethod
  def ClienteExcluir(cls):
    UI.ClienteListar()
    id = int(input("Id do cliente a ser excluído: "))
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)
  @classmethod
  def ServicoInserir(cls):
    descricao = input("Descrição: ")
    valor = input("E-mail: ")
    duracao = input("Duração: ")
    servico = Servico(0, descricao, valor, duracao)
    NServico.inserir(servico)
  @classmethod
  def ServicoListar(cls):
    for servico in NServico.listar():
      print(servico)
  @classmethod
  def ServicoAtualizar(cls):
    UI.ServicoListar()
    id = int(input("Id do serviço a ser atualizado: "))
    descricao = input("Nova descricao: ")
    valor = input("Novo e-mail: ")
    duracao = input("Nova duracao: ")
    servico = Servico(id, descricao, valor, duracao)
    NServico.atualizar(servico)    
  @classmethod
  def ServicoExcluir(cls):
    UI.ServicoListar()
    id = int(input("Id do serviço a ser excluído: "))
    servico = Servico(id, "", "", "")
    NServico.excluir(servico)
  @classmethod
  def AgendaInserir(cls):
    data = datetime.strptime(input("Data: "), "%d/%m/%Y %H:%M")
    agenda = Agenda(0, data, False, 0, 0)
    NAgenda.inserir(agenda)
  @classmethod
  def AgendaListar(cls):
    for agenda in NAgenda.listar():
      print(agenda)
  @classmethod
  def AgendaAtualizar(cls):
    UI.AgendaListar()
    id = int(input("Id da agenda a ser atualizado: "))
    data = datetime.strptime(input("Data: "), "%d/%m/%Y %H:%M")
    agenda = Agenda(id, data, False, 0, 0)
    NAgenda.atualizar(agenda)    
  @classmethod
  def AgendaExcluir(cls):
    UI.AgendaListar()
    id = int(input("Id da agenda a ser excluída: "))
    agenda = Agenda(id, "", "", "", "")
    NAgenda.excluir(agenda)
  @classmethod
  def AbrirAgenda(cls):
        data_txt = input('Data: ')
        data = datetime.strptime(data_txt, '%d/%m/%Y')
        
        while True:
            hora_ini_txt = input('Hora inicial: ')
            hora_ini = datetime.strptime(hora_ini_txt, '%H:%M')
            hora_fin_txt = input('Hora final: ')
            hora_fin = datetime.strptime(hora_fin_txt, '%H:%M')
            
            if hora_ini >= hora_fin:
                print('A hora inicial deve ser menor que a hora final.')
            else: 
                contador_txt = input('Contador: ')
                contador = datetime.strptime(contador_txt, '%H:%M')
                
                while hora_ini <= hora_fin:
                    data_e_horario = datetime(data.year, data.month, data.day, hora_ini.hour, hora_ini.minute)
                    
                    agenda = Agenda(0, data_e_horario, False, 0, 0)
                    NAgenda.inserir(agenda)

                    hora_ini += timedelta(minutes=contador.minute, hours=contador.hour)

                break

UI.Main()