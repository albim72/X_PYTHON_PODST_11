from prostokat import Prostokat
from trojkat import Trojkat
from trapez import Trapez
from kolo import Kolo

pr = Prostokat(4.6,7.8)
print(f"pole prostokąta wynosi: {pr.policz_pole():.2f}")

tr = Trojkat(5.5,8.2)
print(f"pole trójkąta wynosi: {tr.policz_pole():.2f}")

trp = Trapez(6.8,5.1,4.6)
print(f"pole trapezu wynosi: {trp.policz_pole():.2f}")

#Utwórz nowy moduł kolo.py a w nim stwórz klasę Kolo(Figura)
#wyznacza pole koła - według wzoru -> pi*a**2
#zmodyfiuj konstruktor
#policz pole dla promienia wynoszącego 5.5

kl = Kolo(5.5)
print(f"pole koła wynosi: {kl.policz_pole():.2f}")
