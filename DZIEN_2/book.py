class Book:
    #deklaracja stanu(dane) -> konstruktor klasy
    def __init__(self,id,tytul,autor,oprawa,cena=0):
        self.idksiazki = id
        self.tytul = tytul
        self.autor = autor
        self.oprawa = oprawa
        self.cena = cena
        self.wydawnictwo = "Fantazja"
        self.create_book()

    #zachowanie -> funkcje klasy -> metody
    def create_book(self):
        print("tworzenie nowej książki...")

    def print_book(self):
        print(f"książka: {self.tytul}, autor: {self.autor}, cena: {self.cena}, "
              f"oprawa: {self.oprawa}, wydawnictwo: {self.wydawnictwo}")

    def rabat(self):
        return 0.05 * self.cena

    def set_wydaw(self,nowe_wyd):
        self.wydawnictwo = nowe_wyd

    def get_wydaw(self):
        return self.wydawnictwo


b1 = Book(23,"Wiedźmin","Andrzej Sapkowski","twarda",38)
b1.wydawnictwo = "Universe"
b1.print_book()

b12 = Book(24,"Pani Jeziora","Andrzej Sapkowski",40)
b12.set_wydaw("Labirynt")
b12.print_book()

b2 = Book(55,"Hobbit","J.R.R. Tolkien","miękka",32)
b2.print_book()

print(f"wydawnictwo: {b2.get_wydaw()}")
