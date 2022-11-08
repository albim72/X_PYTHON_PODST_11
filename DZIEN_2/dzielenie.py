def podziel(x,y):
    try:
        wynik = (x+1)/(y-2)
    except ZeroDivisionError:
        print("dzielenie przez 0!")
    except NameError:
        print("brak danych")
    except TypeError:
        print("używaj do działania tylko liczby a nie tekst!")
    else:
        print(f"wynik działania: {wynik}")
    finally:
        print("policzmy coś jeszcze.....")

try:
    podziel(1,2)
    podziel(2,1)
    podziel(0.5563,23.9878)
    podziel(True,4)
    podziel(-0.000004,343243)
    podziel(4,False)
    podziel(4,"gjgsdjf")
    podziel(5)
except TypeError:
    print("zbyt mało argumentów, muszą być 2!")

