try:
    #x=23
    x = x*2
except NameError:
    print("x nie istnieje!")
except:
    print("nieokreślony błąd")
else:
    print(f"wartość x wynosi {x}")
finally:
    y = 8
    print(f"wartość y={y}")

print("...ciąg dlaszy programu")
