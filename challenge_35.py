iguais = False
while not iguais:
    X, Y = list(map(int, input().split()))
    if X>Y:
        print("Decrescente")
    elif Y>X:
        print("Crescente")
    else:
        iguais = True