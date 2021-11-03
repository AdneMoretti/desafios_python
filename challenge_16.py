def exames(media):
    exame = float(input())
    print("Nota do exame: {:.1f}".format(exame))
    media = (media+exame)/2

    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print( "Media Final: {:.1f}".format(media))

grades = input()

n1, n2, n3, n4 = grades.split()


media = (2*float(n1)+3*float(n2)+ 4* float(n3)+ float(n4))/10



print("Media: {:.1f}".format(media))
if media >=5 and media <7:
    print("Aluno em exame.")
    exames(media)


if media >= 7:
        print("Aluno aprovado.")

if media < 5:
    print("Aluno reprovado.")


