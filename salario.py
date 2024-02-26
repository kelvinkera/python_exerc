

salario = float(input("Informe seu salário: "))

dez_porcento = salario / 10
quinze = salario / 7

if salario > 1250:
    aumento = salario + dez_porcento
    print("Seu salário com almento será de {}".format(round(aumento,2)))
else:
    salario <= 1250
    aumento_2 = salario + quinze
    print("Seu sarário será de {} reais".format(round(aumento_2,2)))
