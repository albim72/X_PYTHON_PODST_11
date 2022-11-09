#n! = 1*2*...*n
#0! = 1
#?double? max -> 1.8E308 -> 2.3E-324
#?max? n!?? -> 171!
import sys
import math

sys.set_int_max_str_digits(1000000)

def silnia(n):
    if n<0:
        raise ValueError("funkcja silnia jest niezdefiniowana dla liczb ujemnych!")
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

def silnia_rekurencyjna(n):
    if n<0:
        raise ValueError("funkcja silnia jest niezdefiniowana dla liczb ujemnych!")
    if n==0:
        return 1
    else:
        return n*silnia_rekurencyjna(n-1)

try:
    n = int(input("podaj argument n funckji silnia: "))
    print(f"silnia z n = {n} wynosi {silnia(n)}")
    print(f"silnia (math.factorial) z n = {n} wynosi {math.factorial(n)}")
except ValueError as bl:
    print(bl)
