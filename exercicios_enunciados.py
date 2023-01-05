"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# ******************************************************************************
"""numero_int = int (input('Digite um numero inteiro: '))

if numero_int%2 == 0:
    print('Numero correto!')

else:
    print('Numero errado!')
"""
# *******************************************************************************
"""""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# *******************************************************************************
"""""
horario = float (input ('Que horas são: '))

if horario <= 11.59:
    print('Bom dia')

elif horario <= 17.59:
    print('Boa tarde')

else:
    print('Boa noite')
"""
# ********************************************************************************
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# ********************************************************************************


nome = (input('Digite seu primeiro nome: '))
tamanho_nome = len(nome)


if tamanho_nome <= 4:
    print('Seu nome é muito curto')
elif tamanho_nome <=6 and tamanho_nome >= 5:
    print('Seu nome é normal ')
else:
    print('Seu nome é muito grande')
