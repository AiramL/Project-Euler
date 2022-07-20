# Author: Lucas Airam Castro de Souza
# Laboratory: Grupo de Teleinformatica e Automacao (GTA)
# University: Universidade Federal do Rio de Janeiro (UFRJ)



def find_next_prime(prime,prime_numbers):
    verifier = len(prime_numbers) - 1
    next_prime = prime+2
    floor = 1
    while prime_numbers[verifier] > floor:
        if not next_prime%prime_numbers[verifier]:
            verifier = len(prime_numbers) - 1
            next_prime += 2
        else:
            if verifier > 0:
                verifier -= 1
            else:
                return next_prime
    return next_prime

prime_numbers = [2,3]

while len(prime_numbers) < 10001:
        prime_numbers.append(find_next_prime(prime_numbers[-1],prime_numbers))

print(prime_numbers[-1])
