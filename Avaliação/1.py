class Pais():
    def __init__(self, n, p, a):
        self.__nome = ''
        self.__peop = 0
        self.__area = 0

        self.set_nome(n)
        self.set_peop(int(p))
        self.set_area(float(a))

    def set_nome(self, n):
        if n != "":
            self.__nome = n
        else:
            raise ValueError()

    def set_peop(self, p):
        if p >= 0:
            self.__peop = p
        else:
            raise ValueError()

    def set_area(self, a):
        if a >= 0:
            self.__area = a
        else:
            raise ValueError()

    def get_nome(self):
        return self.__nome

    def get_peop(self):
        return self.__peop

    def get_area(self):
        return self.__area

    def calc_dens(self):
        return self.__peop / self.__area

    def __str__(self):
        return f'Pais: {self.__nome} - População: {self.__peop} habitantes - Área: {self.__area} km²'

    def calcular_densidade(pais):
      return pais.calc_dens()


class UI:
    @staticmethod
    def main():
        paises = []
        for i in range(1, 11):
            n = input("Nome do país: ")
            p = int(input("População do país: "))
            a = float(input("Área do país: "))

            pais = Pais(n, p, a)
            paises.append(pais)

            print(pais)
            print(f'Densidade demográfica: {pais.calc_dens():.1f} hab./km²\n')

        pais_maior_densidade = max(paises.calcular_densidade())

        print('Dados do país com maior densidade demográfica:')
        print(f'Nome: {pais_maior_densidade.get_nome()}\nPopulação: {pais_maior_densidade.get_peop()}\nÁrea: {pais_maior_densidade.get_area():.0f} km²\nDensidade demográfica: {pais_maior_densidade.calc_dens():.1f} hab./km²')


UI.main()