def combine_coins(coin='',numbers=[]):
    output=""
    for i in numbers:
        output+= coin+str(i)+" ,"
    return output[:-2]
def combine_coins_one_liner(coin='',numbers=[]):
    return ", ".join([coin+str(i) for i in numbers])
print(combine_coins('$', range(5)))
print(combine_coins_one_liner('$',range(5)))