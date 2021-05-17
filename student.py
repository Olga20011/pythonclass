class Student:
    school="AkiraChix"
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def speak(self):
        return f"Hello class my name is {self.name} " 
    def year_of_birth(self):
        current_year=2021
        return f"Hello class ,i was born {2021-self.age}"       

    