# Exercício - sistema de perguntas e respostas
acertos = 0

def escreve_perguntas(dicionario):
    print(dicionario['Pergunta'])
    print('Opções:')
    i = 0
    for opçao in dicionario['Opções']:
        print(f'{i}) {opçao}')
        i += 1

def corrige_pergunta(dicionario):
    if escolha == dicionario['Resposta']:
        global acertos
        acertos += 1
        print('Acertou ✔')
        
    else:
        print('Errou ⛔')

# Pergunta 01        
pergunta1 = {
    'Pergunta': 'Quantos estados tem o Brasil?',
    'Opções': ['24', '23', '13', '26', '25'],
    'Resposta': '3',
    }
# Pergunta 02
pergunta2 = {
    'Pergunta': 'Qual a capital do Tocantins?',
    'Opções': ['Fortaleza', 'Belém', 'Palmas', 'Recife', 'Salvador'],
    'Resposta': '2',
    }
# Pergunta 03
pergunta3 = {
    'Pergunta': 'Qual foi o primeiro nome do Brasil dado pelos portugueses?',
    'Opções': ['Brazilândia', 'Ilha de Vera Cruz', 'Terra Nova', 'Nova Portugal'],
    'Resposta': '1',
    }
#Pergunta 04
pergunta4 = {
    'Pergunta': 'Quem oficializou a língua portuguesa como língua única do Brasil?',
    'Opções': ['Marques de Pombal', 'Dom Pedro II', 'Dom Pedor I', 'Tira Dentes'],
    'Resposta': '0',
    }
i = 0
while True:
    escreve_perguntas(pergunta1)
    escolha = input('Escolha uma opção: ')
    corrige_pergunta(pergunta1)
    # i += 1
    print()
    escreve_perguntas(pergunta2)
    escolha = input('Escolha uma opção: ')
    corrige_pergunta(pergunta2)
    # i += 1
    print()
    escreve_perguntas(pergunta3)
    escolha = input('Escolha uma opção: ')
    corrige_pergunta(pergunta3)
    # i += 1
    print()
    escreve_perguntas(pergunta4)
    escolha = input('Escolha uma opção: ')
    corrige_pergunta(pergunta4)
    # i += 1
    print()

    print(f'Número de acertos: {acertos}')
    break