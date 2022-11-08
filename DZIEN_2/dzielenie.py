def podziel(x,y):
    try:
        wynik = (x+1)/(y-2)
    except ZeroDivisionError:
        print("dzielenie przez 0!")
    except NameError:
        print("brak danych")
    else:
        print(f"wynik działania: {wynik}")
    finally:
        print("policzmy coś jeszcze.....")
