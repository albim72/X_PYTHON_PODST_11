#import dane
#import dane as dn
from dane import book,stany_mag

from mylib.specdef.kolfunkcje import nowymagazyn,nel_dict

from cls_.miasto import Miasto

print(stany_mag)
print(book)

print(f"książka: {book['tytul']}, autor: {book['autor']}")
print("magazyn nr 2")
print(f"aktualna liczna książek w magazynie po zakupie: {stany_mag[1] -1}")

lst = list(stany_mag)
nowymagazyn(lst,50)

print(lst)

bk = dict(book)
nel_dict(bk,"lakier",True)

print(bk)

ms = Miasto(6,"Rzeszów","podkarpackie")
ms.print_miasto()
