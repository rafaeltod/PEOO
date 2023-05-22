class Pais:
    def __init__(self, n, p, a):
        self.__nome = ''
        self.__populacao = 0
        self.__area = 0

        self.SetNome(n)
        self.SetPopulacao(int(p))
        self.SetArea(float(a))

    def SetNome(self, n):
        if len(n) > 0: self.__nome = n
        else: raise SyntaxError('Esse campo é obrigatório.')
    def SetPopulacao(self, p):
        if p > 0: self.__populacao = p
        else: raise ValueError('A população deve ser um número não nulo.')
    def SetArea(self, a):
        if a > 0: self.__area = a
        else: raise ValueError('A população deve ser um número não nulo.')

    def GetNome(self):
        return self.__nome
    def GetPopulacao(self):
        return self.__populacao
    def GetArea(self):
        return self.__area
    
    
    def Densidade(self):
        return self.__populacao / self.__area
    
    def __str__(self):
        return f'País: {self.__nome} - População: {self.__populacao} - Área: {self.__area:.0f} km^2'
    

class UI:
    def main():
        maior_densidade = 0
        maior_pais = ''
        maior_população = 0
        maior_area = 0
        for i in range(1,11):
            n = input('Digite o nome do país: ')
            p = int(input('Digite a população do país: '))
            a = float(input('Digite a área do país (em km^2): '))

            pais = Pais(n, p, a)

            if pais.Densidade() > maior_densidade: 
                maior_densidade = pais.Densidade()
                maior_pais = n
                maior_população = p
                maior_area = a

            print(pais)
            print(f'Densidade demográfica: {pais.Densidade():.1f} hab./km^2\n')
        
        print('Dados do país com maior densidade demográfica:')
        print(f'Nome: {maior_pais}\nPopulação: {maior_população}\nÁrea: {maior_area:.0f} km^2\nDensidade demográfica: {maior_densidade:.1f} hab./km^2')



UI.main()