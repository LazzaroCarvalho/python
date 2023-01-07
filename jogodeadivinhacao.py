import random
num=float(input('Adivinhe qual numero escolhi de 1 a 10: '))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = random.choice(lista)
if num == random.choice(lista):
    print("Parabens você acertou")
else:
    print("você errou, o numero que escolhi era: ", x)