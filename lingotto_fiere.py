from espositore import Espositore
from stand import *


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__lista_espositori = []
        self.__lista_stand = []
        self.__assegnazioni = dict()



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
                    line = line.rstrip("\n").split(",")
                    if line[0][0:2] == "ST":
                        if len(line) == 5:
                            if line[4].isdigit():  #ho uno stand con prese aggiuntive
                                prezzo_stand_prese_agg = float(line[3]) * (1 + 0.07 * float(line[4]))
                                stand_prese_agg = StandPreseAggiuntive(line[0], line[1], line[2], line[3], prezzo_stand_prese_agg)
                                self.__lista_stand.append(stand_prese_agg)
                            elif line[4].isalpha(): #ho uno stand premium
                                prezzo_stand_premium = float(line[3]) * 1.30
                                stand_premium = StandPremium(line[0], line[1], line[2], line[3], prezzo_stand_premium)
                                self.__lista_stand.append(stand_premium)
                        else:
                            stand_standard = StandStandard(line[0], line[1], line[2], line[3])
                            self.__lista_stand.append(stand_standard)
                    else:
                        espositore = Espositore(line[0], line[1], line[2])
                        self.__lista_espositori.append(espositore)
        except FileNotFoundError:
            raise FileNotFoundError






    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_trovato = None
        for stand in self.__lista_stand:
            if stand.codice_stand == codice_stand:
                stand_trovato = stand
                break

        espositore_trovato = None
        for espositore in self.__lista_espositori:
            if espositore.codice_espositore == codice_espositore:
                espositore_trovato = espositore
                break

        if stand_trovato is None:
            raise ValueError(f"Lo stand {codice_stand} non esiste.")
        if espositore_trovato is None:
            raise ValueError(f"L'espositore {codice_espositore} non esiste.")
        if not stand_trovato.disponibile:
            raise ValueError(f"Lo stand {codice_stand} e' gia' occupato.")
        if codice_espositore in self.__assegnazioni:
            raise ValueError(f"L'espositore {codice_espositore} ha gia' uno stand.")

        stand_trovato.assegna_espositore(espositore_trovato)
        self.__assegnazioni[codice_espositore] = stand_trovato


def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self.__lista_espositori:
            stand = self.__assegnazioni.get(espositore.codice_espositore)
            if stand is None:
                print(f"{espositore} - Nessuno stand assegnato")
            else:
                print(f"{espositore} - Stand assegnato: {stand.codice_stand}")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        lista_stand_ordinata = sorted(self.__lista_stand)
        return lista_stand_ordinata




