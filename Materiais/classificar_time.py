times = ('Athletico-PR', 'Bahia', 'Botafogo', 'Atlético-MG', 'Bragantino', 'Palmeiras', 'Flamengo', 'Chapecoense', 'Internaciona', 'Cruzeiro', 'Grêmio', 'Fortaleza', 'Criciúma', 'Corinthians', 'Juventude', 'Fluminense', 'Vasco', 'Vitória', 'Atlético-GO', 'Cuiabá')
print(f"Lista dos times do Brasileirão: {times}")
print("-="*20)
print(f"Os 5 primeiros são:  {times[0:6]}")
print("-="*20)
print(f"Os 4 últimos são:  {times[16:20]}")
print("-="*20)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-="*20)


for i, nome in enumerate(times):
    posicao = i + 1
    if nome == "Chapecoense":
        print(f"O Chapecoense está na {posicao}ª posição")