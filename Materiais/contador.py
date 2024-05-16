def lin(txt):
    print("~" * 32)
    print(txt)
    print("~" * 32)
    print("")

def contador(inici, fim):
    dez = []
    for i in range(1, 11):
        dez.append(i)
    lin(dez)
   
    dez_zero = []
    zero = 10
    for j in range(6):
        dez_zero.append(zero)
        zero = zero - 2
    print("Contagem de 10 até 0, de 2 em 2:")
    lin(dez_zero)

    personalizada = []
    for i in range(inici, fim +1):
        personalizada.append(i)
    print("Contagem personalizada")
    lin(personalizada)

incial = int(input("Digite um valor inicial da contagem: "))
final = int(input("Digite o valor final da contagem: "))
contador(incial, final)