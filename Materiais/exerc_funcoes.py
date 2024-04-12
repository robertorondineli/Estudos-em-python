# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multoplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado
   

multiplicar1 = multoplicar(3, 4, 88, 1)
print(multiplicar1)

# Crie uma função que fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar

def par_ou_impar(number):
    true_or_false = number % 2 == 0
    if true_or_false:
        return f'O número: {number} é par'     
    
    return f'O número: {number} é ímpar'

print(par_ou_impar(3))
print(par_ou_impar(2))
print(par_ou_impar(1))