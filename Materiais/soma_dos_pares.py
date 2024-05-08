# Uma solução que retorne a soma de todos os elementos pares de uma lista
def soma_par(lista):
    global par
    par = 0
    for numero in lista:
        if (numero % 2) == 0:
            par += numero
    print(f"A soma dos números pares da sua lista é: {par}")

lista = [10, 2, 5, 7, 6, 3]
soma_par(lista)
