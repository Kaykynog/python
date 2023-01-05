import random

def par_impar(number):
    par = number % 2 == 0
    if par:
        return f'{random} é par'
   
    return f'{random} é impar'

random = random.randrange(100)
print (par_impar(random))