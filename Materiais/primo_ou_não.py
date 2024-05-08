# Descobrir se um número é primo ou não
def primo(numero):
    if numero <= 2:
        return False
    for i in range(2, numero):     
        if  numero % i == 0:
            return False                        
    return True    
       
entrada = int(input('Digite um número: '))
if primo(entrada):
    print(f"O número {entrada} é primo")
else:
    print(f"O número {entrada} não é primo")

