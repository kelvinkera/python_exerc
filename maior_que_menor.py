

l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

verificar_triangulo = (l1 < l2 + l3)and(l2 < l1+l3)and(l3 < l1 +l2)


   

if(l1 == l2) and (l2 == l3):
    print("O triângulo é equilátero!")
elif (l1 != l2) and (l2 != l3) and (l1 != l3):
     print("O triângulo é escaleno!")
elif verificar_triangulo:
    print("É um triângulo!")
else:
    print("As medidas não formam um triângulo!")
    


