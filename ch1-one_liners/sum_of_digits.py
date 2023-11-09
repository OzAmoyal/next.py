import functools
def digits_array(num):
    return [int(i) for i in str(num)]
def add(x,y):
    return x+y
def sum_of_digits(num):
    return functools.reduce(lambda x,y:x+y,digits_array(num),0)

print(sum_of_digits(123))