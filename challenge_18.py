linha = input()
A, B = linha.split()
A = int(A)
B = int(B)

if B<A:
    resultado = (24-A)+B
elif A< B:
    resultado = B-A
else:
    resultado = 24
print("O JOGO DUROU ",resultado, "HORA(S)")