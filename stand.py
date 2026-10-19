

class StandStandard:
    def __init__(self, codice_stand, superficie, padiglione, prezzo):
        self.__codice_stand = codice_stand
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo





class StandPreseAggiuntive(StandStandard):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, numero_prese):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__numero_prese = numero_prese




class StandPremium(StandStandard):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, posizione):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__posizione = posizione