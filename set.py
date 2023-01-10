"""s1 = {1, 2, 3, 3, 4, 5} # removendo duplicacação 
print(s1)
"""

# metodos uteis
# add, update, clear, discard
"""s1 = set()
s1.add('Kayky')
s1.add(1)
s1.update(('Olá mundo', 1,2,3,4))

s1.discard('Kayky')
s1.discard('Olá mundo')


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s2 ^ s1
"""
# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite:')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABENS VC ACHOU A LETRA')
        break

    print(letras)




