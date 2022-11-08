from pracownik import Pracownik
from sport import Sport
from empty import Ekstra

class Student(Pracownik,Sport,Ekstra):

    #konstruktor z wielodziedziczeniem
    def __init__(self,imie,wiek,wzrost,waga,nr_studenta,wydzial,kierunek,rokstud,
                 firma,stanowisko,latapracy,dyscyplina,lata_upr,best_wynik):
        Pracownik.__init__(self,imie,wiek,wzrost,waga,firma,stanowisko,latapracy)
        Sport.__init__(self,dyscyplina,lata_upr,best_wynik)
        self.nr_studenta = nr_studenta
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.rokstud = rokstud
        
