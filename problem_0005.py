# Author: Lucas Airam Castro de Souza
# Laboratory: Grupo de Teleinformatica e Automacao (GTA)
# University: Universidade Federal do Rio de Janeiro (UFRJ)



divisors = 20
number = 1

while (True):
    for divisor in range(divisors):
        if number%(divisor+1):
            number+=1
            divisor = 0
            break
    if divisor == divisors-1:
        break

print(number)
