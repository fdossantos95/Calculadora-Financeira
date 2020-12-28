''' Calculos necessários. '''

from time import sleep

def lin():
    print('-'*60)


# Lendo qual é o débito na modalidade Fast:
lin()    
debfast = float(input('Qual é o Debito na modalidade Fast? '))
lin()

# Lendo qual é a RAV na modalidade Fast:
ravfast = float(input('Qual é a RAV na modalidade Fast? ' ))
lin()

# Lendo qual é o crédito a vista na modalidade Fast:
creditoavfast = float(input('Qual é o credito a vista na modalidade Fast? '))
lin()

# Lendo a taxa MDR de 2 a 6X na modalidade Fast:
mdr2a6xfast = float(input('Qual é a MDR 2 a 6X na modalidade Fast? '))
lin()

# Lendo a taxa MDR 7 a 12X na modalidade Fast:
mdr7a12xfast = float(input('Qual é a taxa MDR de 7 a 12X na modalidade Fast? '))
lin()

print(f'O débito na modalidade Fast é {debfast}%')
print(f'A RAV na modalidade Fast é {ravfast}%')
print(f'O crédito a vista na modalidade Fast é {creditoavfast}%')
print(f'A taxa MDR de 2 a 6X na modalidade Fast é {mdr2a6xfast}%')
print(f'A taxa MDR de 7 a 12X na modalidade Fast é {mdr7a12xfast}%')


sleep(2)
lin()
print('Fim')


# Resolver problema dp ponto e da virgula em numeros float, ao digitar no teclado o sistema não aceita virgulas, apenas ponto para separar casas decimais.
# Resolver problema de centralização dos caracteres para apresentação do resultado ao usuário.