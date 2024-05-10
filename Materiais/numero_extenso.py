while True:

    numero = int(input("Digite um número entre 0 e 20: "))
    tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12 ,13, 14, 15, 16, 17, 18, 19, 20)
    extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
    parada = False

    for indice, i in enumerate(tupla):
        if i == numero:
            print(f"{numero} por extenso é: {extenso[indice]}")
            parada = True

    if parada:
        break        
    else:
        print("Número inválido, tente novamente.")
        continue

