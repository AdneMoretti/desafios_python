N = int(input())
for i in range(N):
    escolhaSheldon, escolhaRaj = input().split()
    if((escolhaSheldon == "pedra" and escolhaRaj == "lagarto") or (escolhaSheldon == "papel" and escolhaRaj == "pedra") or 
    (escolhaSheldon == "tesoura" and escolhaRaj == "papel") or (escolhaSheldon == "lagarto" and escolhaRaj == "Spock") or 
    (escolhaSheldon == "Spock" and escolhaRaj == "tesoura") or (escolhaSheldon == "tesoura" and escolhaRaj == "lagarto") or
    (escolhaSheldon == "lagarto" and escolhaRaj == "papel") or (escolhaSheldon == "papel" and escolhaRaj == "Spock") or 
    (escolhaSheldon == "Spock" and escolhaRaj == "papel") or (escolhaSheldon == "pedra" and escolhaRaj == "tesoura")):
        print(f"Caso #{i+1}: Bazinga!")

    elif((escolhaRaj == "pedra" and escolhaSheldon == "lagarto") or (escolhaRaj == "papel" and escolhaSheldon == "pedra") or 
    (escolhaRaj == "tesoura" and escolhaSheldon == "papel") or (escolhaRaj == "lagarto" and escolhaSheldon == "Spock") or 
    (escolhaRaj == "Spock" and escolhaSheldon == "tesoura") or (escolhaRaj == "tesoura" and escolhaSheldon == "lagarto") or
    (escolhaRaj == "lagarto" and escolhaSheldon == "papel") or (escolhaRaj == "papel" and escolhaSheldon == "Spock") or 
    (escolhaRaj == "Spock" and escolhaSheldon == "papel") or (escolhaRaj == "pedra" and escolhaSheldon == "tesoura")):
        print(f"Caso #{i+1}: Raj trapaceou!")
    else:
        print(f"Caso #{i+1}: De novo!")