

n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
n3 = float(input("Informe o terceiro número: "))

if (n1 > n2) and (n1 > n3):
    print("O primeiro número {:.2f} é o maior dos três!".format(n1))
elif (n2 > n1) and (n2 > n3):
    print("O segundo número {:.2f} é o maior dos três!".format(n2))
else:
    (n3 > n1) and (n3 > n2)
    print("O terceiro número {:.2f} é o maior dos três!".format(n3))


if (n1 < n2) and (n1 < n3):
    print("O primeiro número {:.2f} é o menor dos três!".format(n1))
elif (n2 < n1) and (n2 < n3):
    print("O segundo número {:.2f} é o menor dos três!".format(n2))
else:
    (n3 < n1) and (n3 < n2)
    print("O terceiro número {:.2f} é o menor dos três!".format(n3))