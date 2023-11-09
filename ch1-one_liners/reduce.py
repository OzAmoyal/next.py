from functools import reduce

def multiplie(x,y):
    return x*y

def double_Char(str,c):
    return str+c+c
    
def double_letter(my_str):
    return reduce(double_Char,my_str,"")

print(double_letter("hello"))