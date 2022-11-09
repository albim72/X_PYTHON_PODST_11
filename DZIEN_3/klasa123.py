import math


class PierwszaKlasa:
    g = 9.99
    def __init__(self,a:int,b:int):
        self.a=a
        self.b=b

    def print_ab(self):
        print(f"a = {self.a}, b = {self.b}, stała g = {self.g}")


class DrugaKlasa(PierwszaKlasa):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c

    def print_abc(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}, stała g = {self.g}")

    def sumuj(self):
        return self.a+self.b+self.c

class Pierwiastek:
    def pierw_z_sumy(self,suma):
        return math.sqrt(suma)
    
class Potrojenie:
    
    def __init__(self,g,h):
        self.g = g+2
        self.h = h*3
        
    def func_gh(self):
        return self.g*self.h
        
#zadanie: Rozbuduj klasę TrzeciaKlasa o dziedziczenie dodatkowo klas Pierwiastek i Potrojenie
#zmodyfikuj konstruktor klasy
#przepuduj metody:
#1. print_abcd() -> print_abcdgh() -> dodaj wyświetlanie wartości g i h
#2. sumuj() -> a+b+c+d+func_gh()
#Uzupełnij stworzony obiekt tk tak aby uwzględnić zmiany

class TrzeciaKlasa(DrugaKlasa):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d=d

    def print_abcd(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}, d = {self.d}, stała g = {self.g}")

    def sumuj(self):
        return self.a+self.b+self.c+self.d


print("_________ Klasa Pierwsza _____________")
pk = PierwszaKlasa(4,7)
pk.print_ab()
print("_________ Klasa Druga _____________")
dk =DrugaKlasa(5,2,8)
dk.print_ab()
dk.print_abc()
print(f"suma wynosi: {dk.sumuj()}")
print("_________ Klasa Trzecia _____________")
tk = TrzeciaKlasa(7,5,3,9)
tk.print_ab()
tk.print_abc()
tk.print_abcd()
print(f"suma wynosi: {tk.sumuj()}")
