"""
Iterando strings com while
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
cont = 0
asterisco = ''

while cont < len(nome):
    letra = nome[cont]
    asterisco += f'*{letra}'
    cont += 1

asterisco += '*'
print(asterisco)



    
