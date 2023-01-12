# sort não faz ordenação de dicionarios 
# lista.sort() # ordena a minha lista
#sorted(lista)
"""
lista = [
    {'nome': 'Kayky', 'sobrenome': 'Nogueira'},
    {'nome': 'Luiz', 'sobrenome': 'Paulo'},
    {'nome': 'Aline', 'sobrenome': 'Xavier'}
]


def exibir(lista):
    for item in lista:
        print(item) 
    print()

l1 = sorted(lista, key=lambda item: item['nome']) 
l2 = sorted(lista, key=lambda item: item['sobrenome']) 
 
exibir(l1)
exibir(l2) 
"""
def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero + multiplicador
    return multiplica

print(
    executa(
        lambda x, y: x + y,
        2, 3 
    )
)