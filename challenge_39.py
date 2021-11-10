from sys import stdin
import re;
valida = False

for line in stdin:
    letraM = 0
    letram = 0
    numero = 0
    semc=0
    tamanho = len(line) -1
    if tamanho >=6 and tamanho<=32 :
        if(any(letra.isdigit() for letra in line)):
            numero += 1
        if(any(letra.isupper() for letra in line)):
            letram += 1
        if(any(letra.islower() for letra in line)):
            letraM += 1
        if re.match("^[a-zA-Z0-9]*$", line):
            semc+=1
        else:
            semc=0
    
    if letram >0 and letraM>0 and numero>0 and semc>0:
        print("Senha valida")
    else:
        print("Senha invalida")
    valida = False