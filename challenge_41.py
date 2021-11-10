strings =[]
palavra = ""
maior = 0
while(True):
    lista = input().split()
    if(lista[0]=='0'):
        break
    else:
        s = ""
        cont=0
        for item in lista:
            tamanho = len(item)
            if len(item)>=maior:
                maior = tamanho
                palavra = item
            cont+=1            
            if cont != len(lista):
                s = s+f"{tamanho}"+"-"
            else:
                s = s+f"{tamanho}"
                
        print(s)
        #strings.append(s)

#for item in strings:
    #print(item)
print()
print("The biggest word:", palavra)
    