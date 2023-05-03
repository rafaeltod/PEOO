h1, m1 = map(int, input("Digite o primeiro horário no formato hh:mm \n").split(":"))
h2, m2 = map(int, input("Digite o primeiro horário no formato hh:mm \n").split(":"))

totalmin = m1 + m2
totalhrs = h1 + h2

if totalmin >= 60:
  totalmin -= 60
  totalhrs += 1

totalmin = str(totalmin)
if len(totalmin) == 1:
  totalmin = '0' + totalmin

totalhrs = str(totalhrs)
if len(totalmin) == 1:
  totalhrs = '0' + totalhrs

print(f'Total de horas = {totalhrs}:{totalmin}')