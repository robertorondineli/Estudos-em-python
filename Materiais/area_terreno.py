def area(largura, comprimento):
    area = largura * comprimento
    print(f"A área do terreno de {largura}x{comprimento} é: {area:.2f}m²")

larg = float(input("Digite a largura do terreno (em metros): "))
compri = float(input("Digite o comprimento do terreno (em metros): "))
area(larg, compri)

