# Author: Lucas Airam Castro de Souza
# Laboratory: Grupo de Teleinformatica e Automacao (GTA)
# University: Universidade Federal do Rio de Janeiro (UFRJ)

def find_next_prime(prime):
    verifier = prime
    next_prime = prime+1

    while verifier > 1:
        if not next_prime%verifier:
            verifier = next_prime
            next_prime += 1
        else:
            verifier -= 1

    return next_prime

prime_factors = []
current_rest = 600851475143
prime = 2

while current_rest != 1:
    if (not current_rest%prime):
        current_rest /= prime
        prime_factors.append(prime)
    else:
        prime = find_next_prime(prime)

print(prime_factors[-1])
