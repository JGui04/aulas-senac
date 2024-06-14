"""
Construindo Funções para uma calculadora
"""

def soma(a,b):
    resp = a + b
    return resp
def subtracao(a,b):
    return a - b
def multiplicacao(a,b):
    return a * b
def divisao (a,b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por ZERO"

# função para a calculadora
def calculadora():
    print("Bem-vindo a calculadora")
    while True:
        print("Escolha a operação:\n1 - adição\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair\n")
        opcao = int(input("Digite a opção desejada:\n"))

        if (opcao == 5):
            print("\nObrigado por utilizar nossa calculadora!!!")
            break
        
        if (opcao < 1 or opcao > 5):
            print("ERRO - Opção inválida!!!")
        else:
            num1 = float(input("Digite o primeiro número:\n"))
            num2 = float(input("Digite o segundo número:\n"))

            if (opcao == 1):
                result = soma(num1, num2)
                print(f"resultado é {result}")
            elif (opcao == 2):
                result = subtracao(num1, num2)
                print(f"resultado é {result}")
            elif (opcao == 3):
                result = multiplicacao(num1, num2)
                print(f"resultado é {result}")
            elif (opcao == 4):
                result = divisao(num1, num2)
                print(f"resultado é {result}")
            else:
                print("ERRO - Opção inválida!!!")


# chama a função principal
calculadora()


