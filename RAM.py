from pckomponenter import pckomponenter


class RAM(pckomponenter):
    def __init__(self, minne, klokkefrekvens, Type, komponentnavn, produsent, pris):
        super().__init__(Type, komponentnavn, produsent, pris)
        self.minne = minne
        self.klokkefrekvens = klokkefrekvens

    def skrivut(self):
        print("-->", self.Type, "<--")
        print("Minne:", self.minne)
        print("Klokkefrekvens", self.klokkefrekvens)
        super().skrivut()