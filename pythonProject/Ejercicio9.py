# Usando range(1,4) crear una lista y modificarla para que todos sus valores esten al cuadrado

X = []

for j in range(1, 4):
    X.append(j)

print(X)

for i in range(1, 4):
    X[i - 1] = i * i

print(X)


