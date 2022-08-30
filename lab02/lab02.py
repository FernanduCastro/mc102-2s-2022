###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome: fernando castro
# RA:
###################################################

# Leitura de dados
D1_SpaceX = int(input())
V1_SpaceX = int(input())
Time_pass = int(input())
D2_BOrigin = int(input())
V2_BOrigin = int(input())

# Cálculo do tempo total gasto por cada espaçonave 
calcular_spaceX = D1_SpaceX / V1_SpaceX
calcular_BOrigin = (D2_BOrigin / V2_BOrigin) + (Time_pass * 24)

if calcular_spaceX < calcular_BOrigin:
    resultado = True
else:
    resultado = False

# Impressão da resposta
print(resultado)

