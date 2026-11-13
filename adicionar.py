# HelloGit

def adicionar(lista, elemento):
    lista.append(elemento)


def elementos():
    matriz = []

    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break

        idade = int(input("Digite a idade: "))
        adicionar(matriz, [nome, idade])

    return matriz


pessoas = elementos()
print(pessoas)

