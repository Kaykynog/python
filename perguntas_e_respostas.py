# Exercício - sistema de perguntas e respostas
print('Bem vindo ao mini quiz do KAYKY!')
print('Você terá 3 perguntas para responder')
print('Responda com cautela...\n')
import os
os.system("Pause")


perguntas = [
    {
        'Pergunta': 'Qual aumentativo de dacueba?',
        'Opções': ['dacuebasso', 'dacueruim', 'lá ele', 'dacuebao'],
        'Resposta': 'lá ele',
    },
    {
        'Pergunta': 'Quem nasce em Tilambu é o que?',
        'Opções': ['Tilambuquense', 'Tilambuquês', 'Tilambucano', 'lá ele mil vezes'],
        'Resposta': 'lá ele mil vezes',
    },
    {
        'Pergunta': 'Se eu te der 20 CDs de música, você vende 4 pra mim?',
        'Opções': ['sim', 'nao, sou chato', 'claro', 'la ele boy'],
        'Resposta': 'la ele boy',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')