strdata, datai= input().split()
horai, minutoi, segundoi = list(map(int, input().split(" : ")))
strdata, dataf= input().split()
horaf, minutof, segundof= list(map(int, input().split(" : ")))
datai = int(datai)
dataf = int(dataf)
segundostotal = ((dataf*86400)+(horaf*3600) + minutof*60 + segundof) - ((datai*86400)+(horai*3600) + minutoi*60 + segundoi)

if segundostotal <= 0:
    segundostotal= segundostotal + 24*60*60

dias = segundostotal//86400
segundostotal -= dias*86400
horas =  segundostotal//3600
segundostotal -= horas*3600
minutos = segundostotal //60 
segundos = segundostotal%60

print(dias, "dia(s)")
print(horas, "hora(s)")
print(minutos, "minuto(s)")
print(segundos, "segundo(s)")