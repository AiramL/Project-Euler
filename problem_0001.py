# Author: Lucas Airam Castro de Souza
# Laboratory: Grupo de Teleinformatica e Automacao (GTA)
# University: Universidade Federal do Rio de Janeiro (UFRJ)

multiples = [number if (not number%3) or (not number%5) else 0 for number in range(1000)]

print(sum(multiples))
