import requests
from numpy import random
from Pokemon import Pokemon

sorteado = random.randint(897) + 1

x = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(sorteado)).json()

if x['id'] < 152:
    generation = "1ª Geração"
elif x['id'] < 252:
    generation = "2ª Geração"
elif x['id'] < 387:
    generation = "3ª Geração"
elif x['id'] < 494:
    generation = "4ª Geração"
elif x['id'] < 650:
    generation = "5ª Geração"
elif x['id'] < 722:
    generation = "6ª Geração"
elif x['id'] < 810:
    generation = "7ª Geração"
else:
    generation = "8ª Geração"

pok = Pokemon(x['id'], x['name'], x['base_experience'], generation, x['types'])


pok.print_info()

print("akak".join(["1", "2", "3"]))
