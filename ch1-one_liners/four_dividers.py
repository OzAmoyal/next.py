def is_four_dividable(number):
    return number % 4 == 0
def four_dividers(number):
    return filter(is_four_dividable,range(1,number+1))

print(list(four_dividers(10)))

