class UnderAge(Exception):
    def __init__(self, age) -> None:
        super().__init__(age)
        self._age=age

    def __str__(self) -> str:
        return f'You are {self._age} years old, therfore you are under age, please come back in {18-self._age} years'
    

def send_invitation(name, age):
    
    if int(age) < 18:
        raise UnderAge(age)
    else:
        print("You should send an invite to " + name)

try:
    send_invitation('Oz', 20)
    send_invitation('Yossi',17)
except UnderAge as e:
    print(e)