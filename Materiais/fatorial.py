# calcule o fatorial de um número, considere 0! = 1 e 1! = 1
def fatorial(numero):
    if numero != 0 and numero != 1:
        i = 1
        j = numero
        while j > i:
            numero = numero * i
            i += 1
        return numero
    else:
       return 1
valor = int(input('Digite um número: '))
print(f"O fatorial de {valor} é: {fatorial(valor)}")