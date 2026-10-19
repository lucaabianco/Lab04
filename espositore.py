class Espositore:
    def __init__(self, codice_espositore, nome, cognome):
        self.__codice_espositore = codice_espositore
        self.__nome = nome
        self.__cognome = cognome

    @property
    def codice_espositore(self):
        return self.__codice_espositore
    @property
    def nome(self):
        return self.__nome
    @property
    def cognome(self):
        return self.__cognome
    def __str__(self):
        return f"{self.codice_espositore}, {self.nome}, {self.cognome}"