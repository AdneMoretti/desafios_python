valores = input()
id, qnt = valores.split(" ")
qnt = float(qnt)

if id == '1':
    total = qnt* 4.00
if id == '2':
    total = qnt* 4.50
if id == '3':
    total = qnt* 5.00
if id == '4':
    total = qnt* 2.00
if id == '5':
    total = qnt* 1.50

print("Total: R$ {:.2f}".format(total))