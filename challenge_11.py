dados1 = input()
dados2 = input()

code1, qnt1, value1 = (dados1.split(" "))

code2, qnt2, value2 = dados2.split(" ")

total = int(qnt1)*float(value1)+int(qnt2)*float(value2)
print("VALOR A PAGAR: R$ {:.2f}".format(total))