from abc import ABC,abstractmethod

class Postac(ABC):

    def __init__(self,rod,imie,p_zdrowia):
        self.rod = rod
        self.imie = imie
        self.p_zdrowia = p_zdrowia
        self.create_person()

    def create_person(self):
        print(f"członek rodu: {self.rod} -> {self.imie} został utworzony")

    @abstractmethod
    def strata(self):
        pass

    @abstractmethod
    def zysk(self):
        pass

    @abstractmethod
    def set_p_zdr(self,pz):
        self.p_zdrowia = pz


class Lord(Postac):

    def __init__(self,rod,imie,p_zdrowia,p_sily):
        super().__init__(rod,imie,p_zdrowia)
        self.p_sily = p_sily

    def strata(self):
        return self.p_zdrowia - 2

    def zysk(self):
        return self.p_zdrowia + 1

    def set_p_zdr(self, pz):
        super().set_p_zdr(pz)
        


ld = Lord("Lannister","Tywin",8,8)

start = ld.p_zdrowia
print(f"początkowa liczba p zdrowia: {start}")
koniec = ld.strata()
print(f"końcowa liczba p zdrowia: {koniec}")
ld.set_p_zdr(koniec)

print(f"strata zdrowia z {start} punktów, na {ld.p_zdrowia} punktów")

poleczeniu = ld.zysk()
ld.set_p_zdr(poleczeniu)

print(f"zysk zdrowia z {koniec} punktów, na {ld.p_zdrowia} punktów")

