a,c,b,d=list(map(int,input().split()))

dif=((b*60)+d)-((a*60)+c)
if(dif<=0):
    dif+=24*60
    
time=dif//60
minute=dif%60
print(f"O JOGO DUROU {time} HORA(S) E {minute} MINUTO(S)")


horai, minutoi, horaf, minutof = list(map(int, input().split()))
minutostotal = ((horaf*60) + minutof) - ((horai*60)+minutoi)

if minutostotal <= 0:
    minutostotal = minutostotal + 24*60

horas =  minutostotal//60
minutos = minutostotal % 60 


print("O JOGO DUROU",horas, "HORA(S) E", minutos, "MINUTO(S)")