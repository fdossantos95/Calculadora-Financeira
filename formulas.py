''' Calculos necessários. '''

from time import sleep

def lin():
    print('-'*60)


# Lendo itens da simulação Fast:
lin()    
debfast = float(input('Qual é o Debito na modalidade Fast? '))
lin()
ravfast = float(input('Qual é a RAV na modalidade Fast? ' ))
lin()
creditoavfast = float(input('Qual é o credito a vista na modalidade Fast? '))
lin()
mdr2a6xfast = float(input('Qual é a MDR 2 a 6X na modalidade Fast? '))
lin()
mdr7a12xfast = float(input('Qual é a taxa MDR de 7 a 12X na modalidade Fast? '))
lin()

print(f'O débito na modalidade Fast é {debfast}%')
print(f'A RAV na modalidade Fast é {ravfast}%')
print(f'O crédito a vista na modalidade Fast é {creditoavfast}%')
print(f'A taxa MDR de 2 a 6X na modalidade Fast é {mdr2a6xfast}%')
print(f'A taxa MDR de 7 a 12X na modalidade Fast é {mdr7a12xfast}%')
lin()
sleep(2)

# Lendo itens da simulação Sem RAV:
debitosemrav = float(input('Qual é o debito na simulação Sem RAV? '))
lin()
ravsemrav = float(input('Digite zero para simulação Sem RAV: '))
lin()
creditoavsemrav = float(input('Qual é o crédito a vista na simulação Sem RAV? '))
lin()
mdr2a6xsemrav = float(input('Qual é a taxa MDR de 2 a 6X na simulação Sem RAV? '))
lin()
mdr7a12xsemrav = float(input('Qual é a taxa MDR de 7 a 12X na simulação Sem RAV? '))
lin()

print(f'O débito na simulação Sem RAV é {debitosemrav}%')
print(f'A RAV na simulação Sem RAV é {ravsemrav}%')
print(f'O crédito a vista na simulação Sem RAV é {creditoavsemrav}%')
print(f'A taxa MDR de 2 a 6X na simulação Sem RAV é {mdr2a6xsemrav}%')
print(f'A taxa MDR de 7 a 12X na simulação Sem RAV é {mdr7a12xsemrav}%')
lin()

# Lendo itens da simulação Com RAV:
debitocomrav = float(input('Qual é o débito na simulação Com Rav? '))
lin()
ravcomrav = float(input('Qual é a RAV na simulação Com RAV? '))
lin()
creditoavcomrav = float(input('Qual é o crédito a vista na simulação Com RAV? '))
lin()
mdr2a6xcomrav = float(input('Qual é a taxa MDR de 2 a 6X na simulação Com RAV? '))
lin()
mdr7a12xcomrav = float(input('Qual é a taxa MDR de 7 a 12X na simulação Com RAV? '))
lin()

print(f'O débito da simulação Com RAV é {debitocomrav}%')
print(f'A RAV da simulação Com RAV é {ravcomrav}%')
print(f'O crédito a vista da simulação Com RAV é {creditoavcomrav}%')
print(f'A taxa MDR de 2 a 6X na simulação Com RAV é {mdr2a6xcomrav}%')
print(f'A taxa MDR de 7 a 12x na simulação Com RAV é {mdr7a12xcomrav}%')

lin()
sleep(2)
print('Resultado: ')

#Resultado da simulação Fast:
fast2x = 



# Resolver problema dp ponto e da virgula em numeros float, ao digitar no teclado o sistema não aceita virgulas, apenas ponto para separar casas decimais.
# Resolver problema de centralização dos caracteres para apresentação do resultado ao usuário.