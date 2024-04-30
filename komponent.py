from pckomponenter import pckomponenter

class komponent(pckomponenter):
    def __init__(self, komponentnavn, produsent, pris):
        super().__init__(komponentnavn, produsent, pris)
    
    def skrivut(self):
        print("Komponent:")
        super().skrivut()