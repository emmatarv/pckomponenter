class pckomponenter():
    def __init__(self, Type, komponentnavn, produsent, pris):
        self.Type = Type
        self.komponentnavn = komponentnavn
        self.produsent = produsent
        self.pris = pris

    def skrivut(self):
        print("Komponentnavn: ", self.komponentnavn)
        print("Produsent: ", self.produsent)
        print("Pris: ", self.pris)
