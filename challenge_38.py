N = int(input())
mensagem = ""
for i in range(N):
    lista = input().split()
    for item in lista:
        mensagem = mensagem + item[0]
        
    print(mensagem)
    mensagem = ""