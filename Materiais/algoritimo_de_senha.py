# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# Este é um breve script que verifica senha para permitir entrada.


import os

while True:
    try:
        entrada = int(input('Deseja (1)Entrar ou (2)Sair? '))
        if entrada == 1:
            senha = int(input('Digite sua senha númerica: '))
            if senha == 1234:
                os.system('cls')
                print('Bem-vindo(a), você entrou!')
                break
            else:
                print('Senha inválida!\n')
                continue
        else:
            print('Você saiu!')
            break
    except:
        print('Você inseriu dados inválidos!\n')
