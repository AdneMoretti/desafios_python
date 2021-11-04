linha = input()
lista = (linha.split())
lista = list(map(int, lista))
listaordem = sorted(lista)
for item in listaordem:
    print(item)
print()
for item in lista:
    print(item)
