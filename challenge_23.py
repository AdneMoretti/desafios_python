salario = float(input())
imposto = 0
if salario >=0 and salario<= 2000:
    print("Isento")
elif salario>2000:
    if salario > 4500:
        qnt = salario - 4500
        imposto += 0.28* (qnt)
        salario -= qnt
    if salario > 3000 and salario <= 4500:
        qnt = salario - 3000
        imposto += 0.18* (qnt)
        salario -= qnt
    if salario>2000 and salario<=3000: 
        qnt = salario - 2000
        imposto += 0.08* (qnt)
        salario -= qnt

    print("R$ {:.2f}".format(imposto))