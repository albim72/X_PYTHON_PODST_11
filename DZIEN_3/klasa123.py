import math


class PierwszaKlasa:
    gs = 9.99

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def print_ab(self):
        print(f"a = {self.a}, b = {self.b}, stała g = {self.gs}")


class DrugaKlasa(PierwszaKlasa):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def print_abc(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}, stała g = {self.gs}")

    def sumuj(self):
        return self.a + self.b + self.c


class Pierwiastek:
    @staticmethod
    def pierw_z_sumy(suma):
        return math.sqrt(suma)


class Potrojenie:

    def __init__(self, g, h):
        self.g = g + 2
        self.h = h * 3

    def func_gh(self):
        return self.g * self.h


# zadanie: Rozbuduj klasę TrzeciaKlasa o dziedziczenie dodatkowo klas Pierwiastek i Potrojenie
# zmodyfikuj konstruktor klasy
# przepuduj metody:
# 1. print_abcd() -> print_abcdgh() -> dodaj wyświetlanie wartości g i h
# 2. sumuj() -> a+b+c+d+func_gh()
# Uzupełnij stworzony obiekt tk tak aby uwzględnić zmiany

class TrzeciaKlasa(DrugaKlasa, Pierwiastek, Potrojenie):
    def __init__(self, a, b, c, d, g, h):
        DrugaKlasa.__init__(self, a, b, c)
        Potrojenie.__init__(self, g, h)
        self.d = d

    def print_abcdgh(self):
        # print(f"a = {self.a}, b = {self.b}, c = {self.c}, d = {self.d}, "
        #       f"g = {self.g}, h = {self.h}, stała g = {self.gs}")
        return self.a, self.b, self.c, self.d, self.g, self.g, self.gs

    def sumuj(self):
        return self.a + self.b + self.c + self.d + self.func_gh()


print("_________ Klasa Pierwsza _____________")
pk = PierwszaKlasa(4, 7)
pk.print_ab()
print("_________ Klasa Druga _____________")
dk = DrugaKlasa(5, 2, 8)
dk.print_ab()
dk.print_abc()
print(f"suma wynosi: {dk.sumuj()}")
print("_________ Klasa Trzecia _____________")
tk = TrzeciaKlasa(7, 5, 3, 9, 3, 2)
tk.print_ab()
tk.print_abc()
# tk.print_abcdgh()
wynik = tk.print_abcdgh()
print(wynik)
ad, bd, cd, dd, gd, hd, gsd = tk.print_abcdgh()
print(f"a = {ad}, b = {bd}, c = {cd}, d = {dd}, g = {gd}, h = {hd}, stała g = {gsd}")
print(f"suma wynosi: {tk.sumuj()}")
print(Pierwiastek.pierw_z_sumy(45))
print(tk.pierw_z_sumy(tk.sumuj()))
print(Pierwiastek.pierw_z_sumy(tk.sumuj()))
print(Pierwiastek.pierw_z_sumy(6867))
