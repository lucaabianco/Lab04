from espositore import Espositore
from stand import *


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__lista_espositori = []
        self.__lista_stand = []




    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path, "r") as infile:
                for line in infile:
                    line.rstrip("\n").split(",")
                    if line[0][0:1] == "ST":
                        if not line[4]: #ho uno stand standard
                            stand_standard = StandStandard(line[0], line[1], line[2], line[3])
                            self.__lista_stand.append(stand_standard)
                        else:
                            if line[4].isdigit():  #ho uno stand con prese aggiuntive
                                prezzo_stand_prese_agg = float(line[3]) * (1 + 0.7 * float(line[4]))
                                stand_prese_agg = StandPreseAggiuntive(line[0], line[1], line[2], line[3], prezzo_stand_prese_agg)
                                self.__lista_stand.append(stand_prese_agg)
                            elif line[4].isalpha(): #ho uno stand premium
                                prezzo_stand_premium = float(line[3]) * 1.30
                                stand_premium = StandPremium(line[0], line[1], line[2], line[3], prezzo_stand_premium)
                                self.__lista_stand.append(stand_premium)
                    else:
                        espositore = Espositore(line[0], line[1], line[2])
                        self.__lista_espositori.append(espositore)
        except FileNotFoundError:
            raise FileNotFoundError

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
