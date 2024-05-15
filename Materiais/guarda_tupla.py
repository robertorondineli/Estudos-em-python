a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))
d = int(input("Digite o último número: "))
tupla = (a, b, c, d)
# o 9 apareceu x vezes
vezes = tupla.count(9)
print(f"O 9 apareceu {vezes} vezes")
# o 3 apareceu na posição x
if 3 in tupla:
    posicao = tupla.index(3) + 1
    print(f"O número 3 apareceu na posição {posicao}")
# os valores pares digitados foram x x x x
