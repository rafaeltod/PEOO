dia, mes, ano = map(int, input("Digite uma data no formato dd/mm/aaaa \n").split("/"))

meses = { 1: 'janeiro', 2 :'fevereiro', 3 :'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
 
print(f'A data é {dia} de {meses[mes]} de {ano}')