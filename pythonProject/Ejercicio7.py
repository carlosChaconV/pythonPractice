# Programa,una lista X que sustituya cualquier elemento negativo por cero

import random

numbers = []

for x in range(15):
    numbers.append(random.randint(-100, 80))

print(numbers)

numbers2 = []

for num in numbers:
    if num < 0:
        num = 0
    numbers2.append(num)

print(numbers2)

