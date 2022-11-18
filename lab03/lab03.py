###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: FERNANDO CASTRO
# RA: Ingresso do Cinema
###################################################

# leitura de dados

diaSemana = int(input())
horaSessao = str(input())
minutoSessao = str(input())
estudante = input().upper()
formaPagamento = input().upper()

# valor do ingresso inteiro
ingresso = 0
horarioSessao = 1829
horarioInformado = horaSessao + minutoSessao

if int(horarioInformado) <= horarioSessao:
    if diaSemana == 1 or diaSemana ==7:
        ingresso = 30
    elif diaSemana == 2 or diaSemana == 3 or diaSemana == 4:
        ingresso = 15
    elif diaSemana == 5 or diaSemana == 6:
        ingresso = 20

else:
    if diaSemana == 1 or diaSemana == 4 or diaSemana == 5:
        ingresso = 30
    elif diaSemana == 2 or diaSemana == 3:
        ingresso = 20
    elif diaSemana == 6 or diaSemana == 7:
        ingresso = 40

# valor a pagar
if estudante == 'N' and formaPagamento == 'C':
    if int(horarioInformado) <= horarioSessao:
        if diaSemana == 1:
            ingresso -= (ingresso * 0.3)
        elif diaSemana == 2 or diaSemana == 3 or diaSemana == 4 or diaSemana == 5 or diaSemana == 6:
            ingresso -= (ingresso * 0.5)
        elif diaSemana == 7:
            ingresso -= (ingresso * 0.2)

    else:
        if diaSemana == 1 or diaSemana == 6:
            ingresso -= (ingresso * 0.3)
        elif diaSemana == 2 or diaSemana == 3 or diaSemana == 4 or diaSemana == 5:
            ingresso -= (ingresso * 0.5)
        elif diaSemana == 7:
            ingresso -= (ingresso * 0.2)

elif estudante == 'S':
    ingresso -= (ingresso * 0.5)

# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))