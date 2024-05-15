def escreva(txt, tamanho):
    print("~"*tamanho)
    print(txt)
    print("~"*tamanho)


texto = input('Digite seu texto: ')
tam = int(input("Digite o tamano dos traços: "))
escreva(texto, tam)