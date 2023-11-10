import json
from datetime import datetime
from datetime import timedelta
from cliente import Cliente, NCliente
from servico import Servico, NServico
from agenda import Agenda, NAgenda

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