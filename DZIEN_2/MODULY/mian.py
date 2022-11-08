#import dane
#import dane as dn
from dane import book,stany_mag

print(stany_mag)
print(book)

print(f"książka: {book['tytul']}, autor: {book['autor']}")
print("magazyn nr 2")
print(f"aktualna liczna książek w magazynie po zakupie: {stany_mag[1] -1}")
