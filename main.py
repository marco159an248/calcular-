import math
import fractions
import ast
import numpy as np

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Erro: Divisão por zero!")
    return a / b

def potenciacao(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Erro: Não é possível calcular a raiz quadrada de um número negativo!")
    return math.sqrt(a)

def equacao_primeiro_grau(a, b):
    if a == 0:
        raise ValueError("Erro: 'a' não pode ser igual a zero na equação do primeiro grau.")
    return -b / a

def equacao_segundo_grau(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        raise ValueError("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2

def equacao_terceiro_grau(a, b, c, d):
    coeffs = [d, c, b, a]
    roots = np.roots(coeffs)
    return roots

def equacao_quarto_grau(a, b, c, d, e):
    coeffs = [e, d, c, b, a]
    roots = np.roots(coeffs)
    return roots

def equacao_quinto_grau(a, b, c, d, e, f):
    coeffs = [f, e, d, c, b, a]
    roots = np.roots(coeffs)
    return roots

def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("Erro: Peso e altura devem ser valores positivos.")
    imc = peso / altura ** 2
    return imc

def avaliar_expressao(expressao):
    try:
        resultado = eval(expressao)
        return resultado
    except SyntaxError:
        raise ValueError("Erro de sintaxe: Expressão inválida.")
    except NameError as e:
        raise ValueError(f"Erro: Variável não definida: {e}")
    except TypeError as e:
        raise ValueError(f"Erro: {e}")
    except:
        pass
    
    try:
        resultado = ast.literal_eval(expressao)
        return resultado
    except (SyntaxError, ValueError):
        pass
    
    try:
        resultado = eval(expressao, {"__builtins__": None}, {"math": math})
        return resultado
    except:
        raise ValueError("Erro: Não é possível avaliar a expressão com o módulo math.")

def operacoes_com_fracoes(a, b, c, d, operacao):
    frac1 = fractions.Fraction(a, b)
    frac2 = fractions.Fraction(c, d)
    
    if operacao == "+":
        return frac1 + frac2
    elif operacao == "-":
        return frac1 - frac2
    elif operacao == "*":
        return frac1 * frac2
    elif operacao == "/":
        if frac2 == 0:
            raise ValueError("Erro: Divisão por zero!")
        return frac1 / frac2
    else:
        raise ValueError("Erro: Operação inválida.")

def calcular():
    while True:
        print("===================================///")
        print("Bem-vindo à calculadora multi-operações! Selecione uma opção:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potenciação")
        print("6. Raiz Quadrada")
        print("7. Equação do Primeiro Grau")
        print("8. Equação do Segundo Grau")
        print("9. Equação do Terceiro Grau")
        print("10. Equação do Quarto Grau")
        print("11. Equação do Quinto Grau")
        print("12. Calcular IMC")
        print("13. Avaliar Expressão")
        print("14. Operações com Frações")
        print("0. Sair")

        opcao = int(input("Opção selecionada: "))

        if opcao == 0:
            print("Calculadora encerrada.")
            break
        elif opcao == 1:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = soma(a, b)
            print("Resultado:", resultado)
        elif opcao == 2:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = subtracao(a, b)
            print("Resultado:", resultado)
        elif opcao == 3:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = multiplicacao(a, b)
            print("Resultado:", resultado)
        elif opcao == 4:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            try:
                resultado = divisao(a, b)
                print("Resultado:", resultado)
            except ValueError as e:
                print(str(e))
        elif opcao == 5:
            a = float(input("Digite o número base: "))
            b = float(input("Digite o expoente: "))
            resultado = potenciacao(a, b)
            print("Resultado:", resultado)
        elif opcao == 6:
            a = float(input("Digite o número: "))
            try:
                resultado = raiz_quadrada(a)
                print("Resultado:", resultado)
            except ValueError as e:
                print(str(e))
        elif opcao == 7:
            a = float(input("Digite o coeficiente 'a': "))
            b = float(input("Digite o coeficiente 'b': "))
            try:
                resultado = equacao_primeiro_grau(a, b)
                print("Resultado:", resultado)
            except ValueError as e:
                print(str(e))
        elif opcao == 8:
            a = float(input("Digite o coeficiente 'a': "))
            b = float(input("Digite o coeficiente 'b': "))
            c = float(input("Digite o coeficiente 'c': "))
            try:
                resultado = equacao_segundo_grau(a, b, c)
                print("Resultado:", resultado)
            except ValueError as e:
                print(str(e))
        elif opcao == 9:
            a = float(input("Digite o coeficiente 'a': "))
            b = float(input("Digite o coeficiente 'b': "))
            c = float(input("Digite o coeficiente 'c': "))
            d = float(input("Digite o coeficiente 'd': "))
            try:
                resultado = equacao_terceiro_grau(a, b, c, d)
                print("Resultado:", resultado)
            except ValueError as e:
                print(str(e))
        elif opcao == 10:
            a = float(input("Digite o coeficiente 'a': "))
            b = float(input("Digite o coeficiente 'b': "))
            c = float(input("Digite o coeficiente 'c': "))
            d = float(input("Digite o coeficiente 'd': "))
            e = float(input("Digite o coeficiente 'e': "))
            try:
                resultado = equacao_quarto_grau(a, b, c, d, e)
                print("Resultado:", resultado)
            except ValueError as e:
                print(str(e))
        elif opcao == 11:
            a = float(input("Digite o coeficiente 'a': "))
            b = float(input("Digite o coeficiente 'b': "))
            c = float(input("Digite o coeficiente 'c': "))
            d = float(input("Digite o coeficiente 'd': "))
            e = float(input("Digite o coeficiente 'e': "))
            f = float(input("Digite o coeficiente 'f': "))
            try:
                resultado = equacao_quinto_grau(a, b, c, d, e, f)
                print("Resultado:", resultado)
            except ValueError as e:
                print(str(e))
       
        elif opcao == 12:
            peso = float(input("Digite o peso (kg): "))
            altura = float(input("Digite a altura (m): "))
            try:
                resultado = calcular_imc(peso, altura)
                print("Fases de peso:")
                print("Abaixo do peso: 0 -- 19.1")
                print("Peso ideal: 19.1 -- 25.8")
                print("Um pouco acima do peso: 25.8 -- 27.3")
                print("Acima do peso: 27.3 -- 32.3")
                print("Obesidade: 32.3 pra cima")
                print("Resultado:", resultado)
            except ValueError as e:
                print(str(e))

        elif opcao == 13:
            expressao = input("Digite a expressão: ")
            try:
                resultado = avaliar_expressao(expressao)
                print("Resultado:", resultado)
            except ValueError as e:
                print(str(e))
        elif opcao == 14:
            a = int(input("Digite o numerador da primeira fração: "))
            b = int(input("Digite o denominador da primeira fração: "))
            c = int(input("Digite o numerador da segunda fração: "))
            d = int(input("Digite o denominador da segunda fração: "))
            operacao = input("Digite a operação (+, -, *, /): ")
            try:
                resultado = operacoes_com_fracoes(a, b, c, d, operacao)
                print("Resultado:", resultado)
            except ValueError as e:
                print(str(e))
        else:
            print("Opção inválida. Tente novamente.")

calcular()
import math

def arredondamento():
    while True:
        print("____________------------____________------______")
        numero_input = input("Digite um número (ou 's' para sair): ")

        if numero_input.lower() == 's':
            break

        try:
            numero = float(numero_input)
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            continue

        print("Opções de arredondamento:")
        print("1 - Arredondar para cima")
        print("2 - Arredondar para baixo")
        print("3 - Arredondar para cortar decimais")
        print("4 - Arredondamento normal")
        print("5 - Arredondar para o número par mais próximo")
        print("6 - Arredondar para o número ímpar mais próximo")
        print("7 - Arredondar para um número específico de casas decimais")
        print("8 - Arredondar para o número mais próximo com base em uma lista de valores")
        print("9 - Arredondar para o número inteiro mais próximo")
        print("10 - Arredondar para o número mais próximo com base em uma lista de valores e pesos")

        opcao_input = input("Digite o número da opção desejada: ")

        try:
            opcao = int(opcao_input)
        except ValueError:
            print("Opção inválida. Digite um número correspondente a uma opção.")
            continue

        if opcao == 1:
            resultado = math.ceil(numero)
        elif opcao == 2:
            resultado = math.floor(numero)
        elif opcao == 3:
            resultado = int(numero)
        elif opcao == 4:
            resultado = round(numero)
        elif opcao == 5:
            resultado = math.floor(numero) if math.floor(numero) % 2 == 0 else math.ceil(numero)
        elif opcao == 6:
            resultado = math.ceil(numero) if math.ceil(numero) % 2 == 1 else math.floor(numero)
        elif opcao == 7:
            casas_decimais_input = input("Digite o número de casas decimais para arredondar: ")

            try:
                casas_decimais = int(casas_decimais_input)
                if casas_decimais < 0:
                    raise ValueError
            except ValueError:
                print("Número de casas decimais inválido. Digite um número inteiro não negativo.")
                continue

            resultado = round(numero, casas_decimais)
        elif opcao == 8:
            valores_input = input("Digite uma lista de valores separados por espaço: ")
            valores = []

            try:
                valores = [float(x) for x in valores_input.split()]
            except ValueError:
                print("Lista de valores inválida. Digite uma lista válida de valores numéricos.")
                continue

            resultado = min(valores, key=lambda x: abs(x - numero))
        elif opcao == 9:
            resultado = round(numero)
        elif opcao == 10:
            valores_input = input("Digite uma lista de valores separados por espaço: ")
            pesos_input = input("Digite uma lista de pesos correspondentes aos valores separados por espaço: ")

            try:
                valores = [float(x) for x in valores_input.split()]
                pesos = [float(x) for x in pesos_input.split()]
                if len(valores) != len(pesos) or not all(p > 0 for p in pesos):
                    raise ValueError
            except ValueError:
                print("Entrada inválida. Digite listas válidas de valores numéricos e pesos positivos com o mesmo tamanho.")
                continue

            peso_total = sum(pesos)
            resultado = sum([valor * peso for valor, peso in zip(valores, pesos)]) / peso_total
        else:
            print("Opção inválida!")
            continue

        print("Resultado:", resultado)
        print()

arredondamento()

print("Fim do programa")