from pckomponenter import pckomponenter


class CPU(pckomponenter):
    def __init__(self, threads, kjerner, klokkefrekvens, Type, komponentnavn, produsent, pris):
        super().__init__(Type, komponentnavn, produsent, pris)
        self.threads = threads 
        self.kjerner = kjerner
        self.klokkefrekvens = klokkefrekvens

    def skrivut(self):
        print("-->", self.Type, "<--")
        print("Threads:", self.threads)
        print("Kjerner:", self.kjerner)
        print("Klokkefrekvens", self.klokkefrekvens)
        super().skrivut()