# -*- coding: utf-8 -*-
"""000. logicaaa.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YhErtL0hlNWYfcddcfbNUfdZ6unb9Sju

[Logicaaa](https://www.dio.me/articles/lista-de-exercicios-para-treinar-logica-de-programacao)
"""

''' 1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C. '''

A = int(input("Infome valor de A: "))
B = int(input("Informe valor de B: "))
C = int(input("Informe valor de C: "))

soma = A + B

print(f"Soma de A e B = {soma}")

if soma < C:
  print(f"A soma de {A} e {B} é menor que {C}")
else:
  pass

''' 2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo. '''

n = int(input("Informe um numero qualquer: "))

if n %2 == 0:
  print(f"{n} é um numero par")
else:
  print(f"{n} é um numero impar")

# verificar se é possitivo ou negativo
if n >= 0:
  print(f"e  um numero possitivo")
else:
  print(f"e um numero negativo")

''' 3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores,

caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e

imprimir seu valor na tela. '''

A = int(input("Infome valor de A: "))
B = int(input("Informe valor de B: "))

if A == B:
  C = A + B
  print(f"A e B são iguais e sua soma é {C}")
else:
  C = A * B
  print(f"A e B são diferentes, e sua multiplicação é {C}")

''' 4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor. '''

num = int(input("Informe um número: "))

sucessor = num + 1
antecessor = num - 1

print(f"O antecessor de {num} é: {antecessor} o sucessor de {num} é: {sucessor} ")

''' 5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse
usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20). '''
salario_min = 1293.20

salario_usu = float(input("Informe o seu salário: "))

qnt_salario = salario_usu / salario_min

print(f"você tem {qnt_salario:.2f} salarios minimos")

''' 6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.'''

valor = float(input("Informe um valor qualquer em R$: "))
2
reajuste = (valor * 0.05)    ## formular de reajuste de 5%
2
print(f"O reajuste de 5% do valor R$ {valor} é R$ {reajuste} ")

''' 7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO. '''

x = int(input("X: "))
y = int(input("Y: "))

print(x == y)
print(x >= y)
print(x <= y)

''' 8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.'''

v1 = int(input("Valor 1: "))
v2 = int(input("Valor 2: "))
v3 = int(input("Valor 3: "))

# Cria uma lista com os valores e ordena em ordem decrescente
valores = sorted([v1, v2, v3], reverse=True)

# Exibe os valores em ordem decrescente
print("Valores em ordem decrescente:", valores)