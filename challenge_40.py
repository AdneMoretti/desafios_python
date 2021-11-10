N = int(input())
pomekon = []
numpomekon = 151
igual = False
for i in range(N):
    p = input()
 
    for item in pomekon:
        if p == item:
            igual=  True
        
        
    if not igual or len(pomekon)==0:
        pomekon.append(p)
        numpomekon-=1
    
    igual = False

print(pomekon) 
print("Falta(m)", numpomekon, "pomekon(s).")
