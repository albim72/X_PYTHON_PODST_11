from abc import ABC,abstractmethod

class Postac(ABC):

    def __init__(self,rod,imie,p_zdrowia):
        self.rod = rod
        self.imie = imie
        self.p_zdrowia = p_zdrowia
        self.create_person()

    def create_person(self):
        print(f"członek rodu: {self.rod} -> {self.imie} został utworzony")
        
    @abstractmethod
    def strata(self):
        pass
    
    @abstractmethod
    def zysk(self):
        pass
    
    @abstractmethod
    def set_p_zdr(self,pz):
        self.pz = pz
