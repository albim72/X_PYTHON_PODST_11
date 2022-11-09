from figura import Figura
import math

mpi = math.pi

class Kolo(Figura):
    def __init__(self,a):
        super().__init__(a,0)

    def policz_pole(self):
        return mpi*self.a**2
