
def mult_num():
   n1 = float(input("Informe o primeiro número: "))
   n2 = float(input("Informe o segundo número: "))

   opercao_mult = n1 * n2

   return opercao_mult


def div_num():
   n1 = float(input("Informe o primeiro número: "))
   n2 = float(input("Informe o segundo número: "))

   operacao_div = n1 / n2
   
   return operacao_div

def sub_num():
   
   n1 = float(input("Informe o primeiro número: "))
   n2 = float(input("informe o segundo número"))

   operacao_sub = n1 - n2 

   return operacao_sub



def soma_num():
    
    n1 = float(input("Informe o primeiro número: "))
    n2 = float(input("Informe o segundo número: "))
    
    operacao_soma = n1+n2

    return operacao_soma


def main():
   
   continuar = True

   while continuar:
       print("\nEscolha a operação a ser realizada")
       print("1 - Soma")
       print("2 - Subtração")
       print("3 - Divisão")
       print("4 - Multiplicação")
       print("5 - Sair")

       opcao = input("Informe a opção desejada (1-5): ")

       if opcao == "1":
        resultado_s = soma_num()
        print("Resultado da soma é: ", round(resultado_s,2))
    
       elif opcao == "2":
          resultado_sub = sub_num()
          print("O resultado da subtração é: ", round(resultado_sub,2))

       elif opcao == "3":
          resultado_div = div_num()
          print("O resultado da divisão é: ", round(resultado_div,2))
       
       elif opcao == "4":
          resultado_mult = mult_num()
          print("O resultado da multiplicação é: ", round(resultado_mult,2))
       
       elif opcao == "5":
          continuar = False
          print("Saindo...")
       else:
          print("Opção Inválida")


if __name__ == "__main__":
    main()