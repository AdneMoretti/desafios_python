
valido = False
qnt = 0
soma = 0
while not valido or qnt!=2:
    nota = float(input())
    if nota<=10 and nota>=0:
        print("valida")
        qnt+=1
        soma+=nota
        valido = True
    elif nota > 10 or nota<0:
        valido = False
        print("nota invalida")
    
print(f"media = {(soma/qnt):.2f}")