N = int(input())
qnt = 0
lista = []
lista = list(map(int, input().split()))
menor = lista[0]
posicao = 0
for i in range(N):
    if lista[i]<menor:
        menor = lista[i]
        posicao = i
    
print("Menor valor:", menor)
print("Posicao:", posicao)