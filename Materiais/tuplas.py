# Tuplas são imutáveis
# lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata frita")
# print(sorted(lanche))


# for valor, comida in enumerate(lanche):
#     print(valor, comida)

# for valor in range(0, len(lanche)):
#     print(lanche[valor], valor)

# for comida in lanche:
#     print(comida)

a = (1, 2, 3, 4)
b = (5, 6, 7, 7)
c = a + b
print(c.index(2))
print(c.count(7))