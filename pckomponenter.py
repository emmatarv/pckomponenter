
from asyncio.proactor_events import _ProactorDuplexPipeTransport


class kompontenter:
    def __init__(self, komponentnavn, produsent, pris):
        self.komponentnavn = komponentnavn
        self.produsent = produsent
        self.pris = pris

    def vis_komponent(self):
        return f"Komponent: {self.komponentnavn}, \n Produsent: {self.produsent}, \n Pris på komponentet: {self.pris} kr"