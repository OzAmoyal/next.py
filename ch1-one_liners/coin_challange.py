def combine_coins(coin,numbers):
    return (", ").join([coin+str(i) for i in numbers])
print(combine_coins('$', range(5)))