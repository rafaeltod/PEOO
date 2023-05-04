dia, mes, ano = map(int, input("Digite uma data no formato dd/mm/aaaa \n").split("/"))

mesde31dias = [1, 3, 5, 7, 8, 10, 12]
mesde30dias = [4, 6, 9, 11]

ValidarAno = False
ValidarMes = False
ValidarDia = False

if 1900 <= ano <= 2100:
  ValidarAno = True
  
if 1 <= mes <= 12:
  ValidarMes = True

if mes in mesde31dias:
  if 1 <= dia <= 31:
    ValidarDia = True

elif mes in mesde30dias:
  if 1 <= dia <= 30:
    ValidarDia = True

else:
  if 1 <= dia <= 28:
    ValidarDia = True

if ValidarAno and ValidarMes and ValidarDia == True:
 
  print('A data informada é válida')

else:
  print('A data informada não é válida')