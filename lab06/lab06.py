##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: FERNANDO CASTRO
# RA: Torre de Panquecas
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split()]
confirmar = torre[:]
confirmar.sort()

# Leitura e processamento dos movimentos
while True:

    espatulada = int(input())

    if espatulada == 0:
        break

    torre[:espatulada] = torre[espatulada-1::-1]


# Impressão da saída
if torre == confirmar:
    print('Torre estavel')
else:
    print('Torre instavel')