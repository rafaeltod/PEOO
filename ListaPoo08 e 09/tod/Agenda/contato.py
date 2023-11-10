class Contato:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
    def __str__(self):
        return f"{self.__nome} - {self.__email}"