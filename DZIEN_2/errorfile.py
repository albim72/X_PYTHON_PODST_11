import sys

try:
    f = open("waznedane.txt","r",encoding="utf-8")
    s = f.readline()
    i = int(s.strip())
    raise Exception(d=i/0)
except OSError as err:
    print(f"błąd systmowy: {err}")
except ValueError:
    print("nie można przekonwertować danych ze str na int!")
except Exception as ec:
    print(f"jaki to błąd? {type(ec)}")
    print(ec.args)
    print(ec)
except:
    print(f"jaki to błąd? -> {sys.exc_info()[0]}")
