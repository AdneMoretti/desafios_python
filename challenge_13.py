age = int(input())

years = age//365
age-= years*365
month = age//30
age-= month*30
days = age//1

print(years, "ano(s)")
print(month, "mes(es)")
print(days, "dia(s)")