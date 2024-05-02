class FactorialArgumentError(ValueError):
    def __init__(self,arg):
        self._arg=arg
    def __str__(self):
        return f'The argument \'{self._arg}\' of type {type(self._arg)} is not a positive integer'
    def get_arg(self):
        return self._arg

def factorial(n):
    if not isinstance(n,int) or n<0:
        raise FactorialArgumentError(n)
    fact = 1
    for i in range(n,0,-1):
        fact *= i
    return fact
try:
    print(factorial(-1))
except FactorialArgumentError as e:
    print(e)