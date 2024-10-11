#Crie um programa que receba do usuário os valores "a" e "b" e envie para uma função que calcule a função do 1º grau. Ao final, o programa mostre o valor de "x".

# Programa principal :

print("calcular a função em 1 grau")

def calcular_a_funcao_de_1_grau(a1, b2):
    x = -b2 / a1
    return x

a1 = float(input("Digite o valor de 'A': ").replace(",","."))
b2 = float(input("Digite o valor de 'B': ").replace(",","."))

if a1 != 0:
    x = calcular_a_funcao_de_1_grau(a1, b2)
    print(f"O valor de 'X' é: {x}")
else:
    print("O valor de 'A' não pode ser zero.")
