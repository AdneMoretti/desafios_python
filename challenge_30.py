lista = []
for i in range(10):
    numero=int(input())
    lista.append(numero)
    if lista[i] < 0:
        lista[i] = 1
    elif lista[i]==0:
        lista[i] = 1
    print(f"X[{i}] = {lista[i]}")