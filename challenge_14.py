point = float(input())

if point > 25 and point <= 50:
    print("Intervalo (25,50]")
elif point > 0 and point <= 25:
    print("Intervalo [0,25]")
elif point > 50 and point <= 75:
    print("Intervalo (50,75]")
elif point > 75 and point <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")