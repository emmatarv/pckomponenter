class pckomponenter():
    def __init__(self, komponentnavn, produsent, pris):
        self.komponentnavn = komponentnavn
        self.produsent = produsent
        self.pris = pris

    def skrivut(self):
        return f"Komponent: {self.komponentnavn}, \n Produsent: {self.produsent}, \n Pris på komponentet: {self.pris} kr"
