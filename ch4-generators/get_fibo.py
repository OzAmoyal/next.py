def get_fibo():
    a = 0
    b = 1
    while(True):
        yield a
        a, b = b, a+b

fibo_gen = get_fibo()
for i in range(0,10):
    print(next(fibo_gen))