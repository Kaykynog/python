

""" Calculadora com while """

while True:
    print ('Bem vindo a calculadora mais inutil da terra')
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    resultados = 0

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        resultados = num_1_float + num_2_float
        print(resultados)

    elif operador == '-':
        resultados = num_1_float - num_2_float
        print(resultados)
        
    elif operador == '/':
        resultados = num_1_float / num_2_float
        print(resultados)

    elif operador == '*':
        resultados = num_1_float * num_2_float
        print(resultados)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break