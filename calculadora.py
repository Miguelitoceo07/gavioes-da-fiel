# Definindo funções para cada operação
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"
# Função principal da calculadora
def calculadora():
    print("Selecione o número da operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(num1, "+", num2, "=", soma(num1, num2))
    elif escolha == '2':
        print(num1, "-", num2, "=", subtracao(num1, num2))
    elif escolha == '3':
        print(num1, "*", num2, "=", multiplicacao(num1, num2))
    elif escolha == '4':
        print(num1, "/", num2, "=", divisao(num1, num2))
    else:
        print("Opção inválida!")
#  Chamando a função principal da calculadora
calculadora()
import math  # Importando o módulo math para usar a função sqrt (raiz quadrada)

# Definindo funções para cada operação
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def raiz_quadrada(a):
    return math.sqrt(a)

# Função principal da calculadora
def calculadora():
    print("Selecione o número da operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Raiz Quadrada")  # Adicionando a opção de raiz quadrada

    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha in ['1', '2', '3', '4']:  # Para operações que necessitam de dois números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(num1, "+", num2, "=", soma(num1, num2))
        elif escolha == '2':
            print(num1, "-", num2, "=", subtracao(num1, num2))
        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicacao(num1, num2))
        elif escolha == '4':
            print(num1, "/", num2, "=", divisao(num1, num2))
    elif escolha == '5':  # Para a operação de raiz quadrada que necessita de um número
        num = float(input("Digite o número para calcular a raiz quadrada: "))
        print("Raiz quadrada de", num, "=", raiz_quadrada(num))
    else:
        print("Opção inválida!")

# Chamando a função principal da calculadora
calculadora()
