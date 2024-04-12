# Exercícios
# crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def gerar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = gerar_multiplicador(2)
triplicar = gerar_multiplicador(3)
quadruplicar = gerar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))