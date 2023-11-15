class BigThing:
    def __init__(self,thing):
        self._thing=thing

    def size(self):
        if isinstance(self._thing,int):
            return self._thing
        elif isinstance(self._thing,dict) or isinstance(self._thing,list) or isinstance(self._thing,str):
            return len(self._thing)
