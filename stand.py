class StandStandard:
    disponibile = True
    def __init__(self, codice_stand, superficie, padiglione, prezzo):
        self.__codice_stand = codice_stand
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo
        self.disponibile = True
        self.__espositore = None

    @property
    def codice_stand(self):
        return self.__codice_stand

    @property
    def superficie(self):
        return self.__superficie

    @property
    def padiglione(self):
        return self.__padiglione

    @property
    def prezzo(self):
        return self.__prezzo

    @property
    def espositore(self):
        return self.__espositore

    def assegna_espositore(self, espositore):
        """Memorizza l'espositore assegnato e rende lo stand non disponibile."""
        if not self.disponibile:
            raise ValueError(f"Lo stand {self.codice_stand} non e' disponibile.")
        self.__espositore = espositore
        self.disponibile = False

    def __lt__(self, other):
        if not isinstance(other, StandStandard):
            return NotImplemented
        return self.prezzo < other.prezzo

    def _descrizione(self, tipologia, dettaglio=""):
        testo = (f"{self.codice_stand}: {tipologia} | {self.superficie:g} mq - "
                 f"Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€")
        if dettaglio:
            testo += f" - {dettaglio}"
        stato = "Disponibile" if self.disponibile else "Non disponibile"
        return f"{testo} - {stato}"

    def __str__(self):
        return self._descrizione("Standard")

    def __repr__(self):
        return str(self)

class StandPreseAggiuntive(StandStandard):
    disponibile = True
    def __init__(self, codice_stand, superficie, padiglione, prezzo, numero_prese):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__numero_prese = numero_prese


class StandPremium(StandStandard):
    disponibile = True
    def __init__(self, codice_stand, superficie, padiglione, prezzo, posizione):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__posizione = posizione


