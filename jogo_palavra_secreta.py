
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra = 'salgadinho'
digitado = []
chances = 10

print('*' * 90)
print('Bem vindo ao joguinho do Kayky, você terá 10 chances para acertar a palavra secreta! \nSera que você consegue? ')
print('*' * 90)
print('Dica: é de comer!\n')

import os   
os.system("pause")


while True:
    
    letra = str(input('Digite uma letra: '))

    if len (letra) > 1:
        print('Digita só uma letra cara ;)')
        continue
    
    digitado.append (letra)

    secreto_temporario = ''

    for letra_forca in palavra:
        if letra_forca in digitado:
            secreto_temporario += letra_forca
        else:
            secreto_temporario += '*'

    if secreto_temporario == palavra:
        
        print('Parabens, voce ganhou! \n' 'A Palavra era :', palavra)
        break

    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in palavra:
        chances -= 1

    if chances == 0:
        print('Você perdeu ;( que pena')
        break

print(f'voce ainda tinha {chances} chances \n')
