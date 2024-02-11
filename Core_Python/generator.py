import json
import random

animals = json.load(open("animals.txt"))
adjectives = json.load(open("adjectives.txt"))

randomAdj = ""
if (random.randint(1, 2) == 1):
    randomAdj = adjectives[random.randint(0,len(adjectives))] + " "
randomAnimal = animals[random.randint(0,len(animals))]
print("The " + randomAdj + randomAnimal)