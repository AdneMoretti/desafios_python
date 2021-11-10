N = int(input())
valido = True
for i in range(N):
    RA = input()

    if len(RA) != 20 or RA[0:2] != "RA":
        valido =  False
    else:
        print(int(RA[2:20]))
    
if not valido:
    print("INVALID DATA")  