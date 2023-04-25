def formatar_nome(nome):
  palavras = nome.split()
  resultado = ''
  for palavra in palavras:
      resultado += palavra.capitalize() + ' '
  return resultado.strip()
print(formatar_nome("julio cesar"))