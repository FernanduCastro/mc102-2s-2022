###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: FERNANDO CASTRO
# RA: DONT KNOW WTF IS THIS!
###################################################

# leitura da sequência de compras e vendas
Borabill = True
estoque = 0
vendas = 0
while Borabill == True:
    
    entrada = int(input())

    if entrada != 0:
        if entrada > 0: #(entrada +)
            if estoque >= 0: #(estoque +)
                estoque += entrada
        elif entrada < 0: #(entrada -)
            if estoque > 0: #(estoque +)
                if (estoque + entrada ) < 0:
                    print(f'Quantidade indisponível para a venda de {entrada*-1} unidades.')
                    estoque = estoque
                else:
                    estoque += entrada
                    vendas += 1
            else: #(estoque -)
                print(f'Quantidade indisponível para a venda de {entrada*-1} unidades.')
                estoque = estoque

    else:
        Borabill = False

# impressão da saída
print(f'Quantidade de vendas realizadas: {vendas}')
print(f'Quantidade em estoque: {estoque}')