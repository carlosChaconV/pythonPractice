# Lista aleatoria que genere listas impar y par
import random

numbers = []
par = []
impar = []

for x in range(15):
    numbers.append(random.randint(0, 100))

for num in numbers:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(numbers)
print(f'lista par: {par}')
print(f'lista impar: {impar}')