class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
    def calc_area(self):
        return self.__base * self.__altura
    def calc_diagonal(self):
        return ((self.__base ** 2 + self.__altura ** 2) ** 0.5)
    def __str__(self):
        return f"Base = {self.__base} - Altura = {self.__altura}"