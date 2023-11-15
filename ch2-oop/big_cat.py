from big_thing import BigThing
class BigCat(BigThing):
    def __init__(self, thing,weight):
        super().__init__(thing)
        self._weight=weight
    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "OK"
        
def main():
    cutie = BigCat("mitzy", 22)
    print(cutie.size())
main()