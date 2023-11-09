import math
def is_prime(number):
 # use list comprehension to generate a list of all the number dividers
 # if the length of the list is 0 it means its prime
 return len([x for x in range(2,int(math.sqrt(number)+1)) if number%x==0])==0

print(is_prime(42)) #False
print(is_prime(43)) #True