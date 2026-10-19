class StandStandard:
    def __init__(self, codice_stand, superficie, padiglione, prezzo):
        self.__codice_stand = codice_stand
        self.__superficie = float(superficie)
        self.__padiglione = int(padiglione)
        self.__prezzo = float(prezzo)
        self.disponibile = True
        self.__espositore = None

    @property
    def codice_stand(self):
        return self.__codice_stand

    @property
    def prezzo(self):
        return self.__prezzo

    @property
    def espositore(self):
        return self.__espositore

    def assegna_espositore(self, espositore):
        if not self.disponibile:
            raise Exception(f"Lo stand {self.__codice_stand} e' gia' occupato.")
        self.__espositore = espositore
        self.disponibile = False

    def __lt__(self, other):
        if not isinstance(other, StandStandard):
            return NotImplemented
        return self.__prezzo < other.prezzo

    def _descrizione(self, tipo, dettaglio=""):
        testo = (f"{self.__codice_stand}: {tipo} | "
                 f"{self.__superficie:g} mq - Padiglione {self.__padiglione} "
                 f"- Prezzo {self.__prezzo:.2f}€")
        if dettaglio:
            testo += f" - {dettaglio}"
        stato = "Disponibile" if self.disponibile else "Non disponibile"
        return f"{testo} - {stato}"

    def __str__(self):
        return self._descrizione("Standard")

    def __repr__(self):
        return self.__str__()


class StandPreseAggiuntive(StandStandard):
    def __init__(self, codice_stand, superficie,padiglione, prezzo, numero_prese):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__numero_prese = int(numero_prese)

    @property
    def numero_prese(self):
        return self.__numero_prese

    @numero_prese.setter
    def numero_prese(self, numero):
        self.__numero_prese = int(numero)

    def __str__(self):
        dettaglio = (f"Prese aggiuntive: {self.__numero_prese}"
                    if self.__numero_prese is not None
                    else "Prese aggiuntive: da completare")
        return self._descrizione("Prese Extra", dettaglio)


class StandPremium(StandStandard):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, posizione):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__posizione = posizione

    @property
    def posizione(self):
        return self.__posizione

    @posizione.setter
    def posizione(self, posizione):
        self.__posizione = posizione

    def __str__(self):
        dettaglio = (f"Posizione: {self.__posizione}"
                    if self.__posizione is not None
                    else "Posizione: da completare")
        return self._descrizione("Premium", dettaglio)