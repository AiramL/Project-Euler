# Author: Lucas Airam Castro de Souza
# Laboratory: Grupo de Teleinformatica e Automacao (GTA)
# University: Universidade Federal do Rio de Janeiro (UFRJ)

from itertools import permutations

def is_prime(prime):
    verifier = prime - 1
    while verifier > 1:
        if not prime%verifier:
            return False
        else:
            verifier -= 1
    return True

def verify_pandigit(number,digit):
    if len(str(number)) != digit:
        return False

    for n in range(1,digit+1):
        if str(n) not in str(number):
            return False
    return True

numbers = list(permutations([7,6,5,4,3,2,1]))
strings = []

for permutation in numbers:
    number_string = ''
    for digit in permutation:
        number_string += str(digit)
    print('verifying the number: '+number_string)
    if is_prime(int(number_string)):
        if verify_pandigit(int(number_string),7):
            print(number_string)
            break

