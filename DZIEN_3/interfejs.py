from abc import ABCMeta, abstractmethod


class IPojazd(metaclass=ABCMeta):

    @abstractmethod
    def spalanie(self, odl, litry): raise NotImplementedError

    @abstractmethod
    def kosztprzejazdu(self, odl, litry, cena_l): raise NotImplementedError


class Pojazd(IPojazd):
    def spalanie(self, odl, litry):
        return litry * 100 / odl

    def kosztprzejazdu(self, odl, litry, cena_l):
        return self.spalanie(odl, litry) * (odl / 100) * cena_l

p1 = Pojazd()
odl = float(input("podaj odlgłość [km]: "))
lt = float(input("podaj ilość spalonego paliwa w [l]: "))
cn_l = float(input("podaj cenę za litr paliwa: "))

print(f"spalanie [l/100km]: {p1.spalanie(odl,lt):.2f}")
print(f"koszt prejazdu na trasie: {odl} km wynosi {p1.kosztprzejazdu(odl,lt,cn_l):.2f} zł")
