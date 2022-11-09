liczby = [56,89,90,24,122,1009,-344,0,199,-333,900,1230]

def stats(dane):
    minimum = min(dane)
    maksimum = max(dane)
    rozstep = maksimum - minimum
    licz_elem = len(dane)
    sr_arytm = sum(dane)/licz_elem
    return minimum,maksimum,rozstep,licz_elem,sr_arytm

wynik = stats(liczby)
print(wynik)

mini,maxi,roz,lel,artm = stats(liczby)
print(f"wartość największa: {maxi}, wartość najmniejsza: {mini}, rozstęp: {roz}, "
      f"liczba elementów kolekcji: {lel}, średnia arytmetyczna: {artm}")
