from prostokat import Prostokat
from trojkat import Trojkat
from trapez import Trapez

pr = Prostokat(4.6,7.8)
print(f"pole prostokąta wynosi: {pr.policz_pole():.2f}")

tr = Trojkat(5.5,8.2)
print(f"pole trójkąta wynosi: {tr.policz_pole():.2f}")

trp = Trapez(6.8,5.1,4.6)
print(f"pole trapezu wynosi: {trp.policz_pole():.2f}")
