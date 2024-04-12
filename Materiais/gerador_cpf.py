# #Este código calcula os digitos do cpf e compara para validar o mesmo
numero_do_cpf1 = []
cpf_tratado = []

def editar_cpf(a):
    b = ''
    i = 0
    j = 0
    while i <= 10:
        b += a[j]
        if len(b) == 3:
            b += '.'
        if len(b) == 7:
            b += '.'
        if len(b) == 11:
            b += '-'
        i += 1
        j += 1
    print(f'CPF gerado: {b}')

while True:
    try:
        operador = int(input('Escolha uma operação:'
            '\n(1)Validar CPF\n(2)Gerar CPF\nEscolha: '))
    except:
        print('Você digitou dados inválidos!\n')
        continue
    if operador == 1:
        try:      
            numero_do_cpf = input('Digite seu CPF(123.123.123-12): ')
            for digit_por_digit in numero_do_cpf:
                numero_do_cpf1.append(digit_por_digit)

            del numero_do_cpf1 [3]
            del numero_do_cpf1 [6]
            del numero_do_cpf1 [9]

            for num_do_cpf in numero_do_cpf1:
                cpf_tratado.append(int(num_do_cpf))
        except:
            print('Por digite dados válidos')
            continue
        #Neste bloco é feito o cálculo do primeiro digito
        i = 0
        j = 0
        soma = 0
        multiplicador = 10
        while i <=8:
            soma += (multiplicador * cpf_tratado[j])
            
            i += 1
            j += 1
            multiplicador -= 1
            
        primeiro_digito = (soma * 10) % 11
        if primeiro_digito > 9:
            primeiro_digito = 0

        #Neste bloco é feito o cálculo do segundo digito
        k = 0
        l = 0
        soma2 = 0
        multiplicador2 = 11
        while k <=9:
            soma2 += (multiplicador2 * cpf_tratado[l])
            k += 1
            l += 1
            multiplicador2 -= 1
        
        segundo_digito = (soma2 * 10) % 11
        if segundo_digito > 9:
            segundo_digito = 0

        #Neste bloco é o cpf inserido pelo user é comparado com o cpf gerado
        cpf_gerado_calculo  = []

        for num_por_num_tradado in cpf_tratado:
            cpf_gerado_calculo.append(num_por_num_tradado)
        
        del cpf_gerado_calculo[10]
        del cpf_gerado_calculo[9]
        cpf_gerado_calculo.append(primeiro_digito)
        cpf_gerado_calculo.append(segundo_digito)

        if cpf_tratado == cpf_gerado_calculo:
            print('CPF válido')
        else:
            print('CPF inválido')

    elif operador == 2:
        import random

        nove_digitos = ''

        for i in range(9):
            nove_digitos += str(random.randint(0, 9))

        contador_regressivo_1 = 10

        resultado_digito_1 = 0
        for digito in nove_digitos:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11

        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

        editar_cpf(cpf_gerado_pelo_calculo)



    sair = input('\nDeseja realizar mais uma operção? (1)Sim (2)Não: ')
    if sair == '2':
        break
    else:
        continue




