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
