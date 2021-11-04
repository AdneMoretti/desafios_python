salary = float(input())
if salary >= 0 and salary <= 400.00:
    readjustment = 0.15 * salary
    salary = salary+readjustment
    percentual = '15 %'
elif salary > 400.00 and salary <= 800.00:
    readjustment = 0.12 * salary
    salary += readjustment
    percentual = '12 %'
elif salary > 800.00 and salary <=1200 :
    readjustment = 0.10 * salary
    salary += readjustment
    percentual = '10 %'
elif salary > 1200 and salary <= 2000:
    readjustment = 0.07 * salary
    salary += readjustment
    percentual = '7 %'
elif salary > 2000.0:
    readjustment = 0.04 * salary
    salary += readjustment
    percentual = '4 %'

print("Novo salario: {:.2f}".format(salary)) 
print("Reajuste ganho: {:.2f}".format(readjustment))
print("Em percentual:", percentual)