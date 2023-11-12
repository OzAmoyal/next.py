class octopus:
    count_animals=0
    def __init__(self,name="Octavio"):
        self._name=name
        self._age=0
        octopus.count_animals+=1
    def birthday(self):
        self._age+=1
    
    def get_age(self):
        return self._age
    def set_name(self,name):
        self._name=name
    
    def get_name(self):
        return self._name
    
    
Octavio = octopus()
Luther = octopus ("Luther")
Octavio.birthday()
print(Octavio.get_age())
print(Luther.get_age())
Luther.set_name("yosi")
print(Luther.get_name())
print("num of animals:",octopus.count_animals)