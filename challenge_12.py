stringnotas = ['100,00', '50,00', '20,00', '10,00', '5,00', '2,00', '1,00']

notas = []

A = int(input())
a = A


notas.append(A//100)
A = A - notas[0] * 100
notas.append(A//50)
A = A - notas[1]* 50
notas.append(A//20)
A = A - notas[2]*20
notas.append(A//10)
A = A - notas[3] * 10
notas.append(A//5)
A = A - notas[4]* 5
notas.append(A//2)
A = A - notas[5] * 2
notas.append(A//1)

for i in range(7):
    print(a)
    print(notas[i], "nota(s) de R$", stringnotas[i])

