from pracownik import Pracownik
from sport import Sport
from empty import Ekstra

class Student(Pracownik,Sport,Ekstra):

    #konstruktor z wielodziedziczeniem
    def __init__(self,imie,wiek,wzrost,waga,nr_studenta,wydzial,kierunek,rokstud,
                 firma="",stanowisko="",latapracy="",dyscyplina="",lata_upr="",best_wynik=""):
        Pracownik.__init__(self,imie,wiek,wzrost,waga,firma,stanowisko,latapracy,0)
        Sport.__init__(self,dyscyplina,lata_upr,best_wynik)
        self.nr_studenta = nr_studenta
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.rokstud = rokstud

    # def __init__(self,nr_studenta,wydzial,kierunek,rokstud):
    #     self.nr_studenta = nr_studenta
    #     self.wydzial = wydzial
    #     self.kierunek = kierunek
    #     self.rokstud = rokstud
    
    def print_student(self):
        print(f"dane studenta -> id: {self.nr_studenta}, wydział: {self.wydzial}, kierunek: {self.kierunek}, "
              f"rok studiów: {self.rokstud}")

    def czypracownik(self):
        return self.firma != ""
        
    
