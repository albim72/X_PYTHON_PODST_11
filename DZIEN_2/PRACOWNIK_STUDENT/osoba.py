class Osoba:

    def __init__(self,imie,wiek,wzrost,waga):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.waga = waga
        self.kolor_oczu = "brązowy"
        self.info()

    def info(self):
        print("powstał obiekt klasy Osoba....")

    def print_osoba(self):
        print(f"osoba -> imię: {self.imie}, wiek: {self.wiek}, wzrost: {self.wzrost} cm, "
              f"waga: {self.waga} kg.")

    def wiekza10lat(self):
        return self.wiek + 10

    def czypracownik(self):
        return False
    
    def bmi(self):
        return self.waga/(self.wzrost/100)**2
    
    def opis_bmi(self):
        if self.bmi()<18.5:
            return "niedowaga"
        elif self.bmi()<=25:
            return "waga prawidłowa"
        elif self.bmi()<=30:
            return "nadwaga"
        else:
            return "otyłość"
