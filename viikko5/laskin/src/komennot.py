class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._edellinen_arvo = 0

    def suorita(self):
        try:
            self._edellinen_arvo = self._sovelluslogiikka.arvo()
            arvo = int(self._lue_syote())
            self._sovelluslogiikka.plus(arvo)
        except:
            pass

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)


class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._edellinen_arvo = 0

    def suorita(self):
        try:
            self._edellinen_arvo = self._sovelluslogiikka.arvo()
            arvo = int(self._lue_syote())
            self._sovelluslogiikka.miinus(arvo)
        except:
            pass

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)


class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)


class Kumoa:
    def __init__(self, sovelluslogiikka, viimeisin_komento):
        self._sovelluslogiikka = sovelluslogiikka
        self._viimeisin_komento = viimeisin_komento

    def suorita(self):
        viimeisin_komento = self._viimeisin_komento()
        if viimeisin_komento:
            viimeisin_komento.kumoa()

    def aseta_viimeisin_komento(self, komento):
        self._viimeisin_komento = komento
