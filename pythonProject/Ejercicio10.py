
import random

numbers = []

for x in range(20):
    numbers.append(random.randint(1, 10))

print(numbers)

numbers.reverse()

print(numbers)