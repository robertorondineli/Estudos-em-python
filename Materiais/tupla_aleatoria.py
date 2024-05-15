import random

tupla = tuple(random.randint(1, 9) for _ in range(5))
print(tupla)
maior = max(tupla)
menor = min(tupla)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")