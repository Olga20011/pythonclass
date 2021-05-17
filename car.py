class Car:
    def __init__(self,make,colour):
        self.make=make
        self.colour=colour
    def speed(self):
        return f"My  {self.colour} {self.make}  moves at 40km/hr" 
    def hooting(self):
        print("peeeeeeeep peeeeeep")    
        