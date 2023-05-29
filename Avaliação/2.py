class PeçaDominó:
    def __init__(self, u, d):
        self.__l1 = 0
        self.__l2 = 0

        self.set_lado1(u)
        self.set_lado2(d)

    def set_lado1(self, u):
        if 0 <= u <= 6:
            self.__l1 = u
        else:
            raise ValueError("Valor inválido para o lado 1.")

    def set_lado2(self, d):
        if 0 <= d <= 6:
            self.__l2 = d
        else:
            raise ValueError("Valor inválido para o lado 2.")

    def get_lado1(self):
        return self.__l1

    def get_lado2(self):
        return self.__l2

    def combinar(self, pd):
        if self.__l1 == pd.get_lado1() or self.__l1 == pd.get_lado2() or \
                self.__l2 == pd.get_lado1() or self.__l2 == pd.get_lado2():
            return True
        else:
            return False

    def __str__(self):
        return f'[{self.__l1} | {self.__l2}]'


class UI:
    @staticmethod
    def main():
        u1 = int(input("Digite o valor para o lado 1 da primeira peça: "))
        d1 = int(input("Digite o valor para o lado 2 da primeira peça: "))
        peca1 = PeçaDominó(u1, d1)

        u2 = int(input("Digite o valor para o lado 1 da segunda peça: "))
        d2 = int(input("Digite o valor para o lado 2 da segunda peça: "))
        peca2 = PeçaDominó(u2, d2)

        print("Primeira peça: \n", peca1)
        print("Segunda peça: \n", peca2)

        if peca1.combinar(peca2):
            print("As peças combinam.")
        else:
            print("As peças não combinam.")
          
UI.main()
