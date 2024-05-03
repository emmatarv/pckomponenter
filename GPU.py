from pckomponenter import pckomponenter


class GPU(pckomponenter):
    def __init__(self, vram, klokkefrekvens, grensesnitt, Type, komponentnavn, produsent, pris):
        super().__init__(Type, komponentnavn, produsent, pris)
        self.vram = vram
        self.klokkefrekvens = klokkefrekvens
        self.grensesnitt = grensesnitt

    def skrivut(self):
        print("-->", self.Type, "<--")
        print("VRAM: ", self.vram)
        print("Klokkefrekvens: ", self.klokkefrekvens)
        print("Grensesnitt: ", self.grensesnitt)
        super().skrivut()