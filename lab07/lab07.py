###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome: FERNANDO CASTRO
# RA: Disconnect
###################################################

# Leitura das tropas de defesa
qtd_Defesa = int(input())
lista_Defesa = [int(input()) for i in range(qtd_Defesa)]

# Leitura das tropas de ataque
qtd_Atack = int(input())
lista_Atack = [int(input()) for i in range(qtd_Atack)]

# Processamento da guerra
posicao = 0

while True:

  proximo = 0
  Vitoria = 0
  Empate = 0
  Derrota = 0
    
  posicao += 1

  if len(lista_Defesa) < len(lista_Atack):
    print('Derrota')
    break

  for numero in lista_Atack:

    if numero > lista_Defesa[proximo]:
      Vitoria += 1

    elif numero == lista_Defesa[proximo]:
      Empate += 1

    else:
      Derrota +=1
        
    proximo += 1

  if Derrota >= Vitoria:
    lista_Defesa.pop(0)

  else:
    print('Vitória posicionando as tropas a partir da posição', posicao)
    break
