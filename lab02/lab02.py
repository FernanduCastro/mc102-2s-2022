###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome: fernando castro
# RA:
###################################################

# Leitura de dados
D1_SpaceX = int(input('Distância da trajetória, em quilômetros (km), entre a Terra e Marte no lançamento da SpaceX: '))
V1_SpaceX = int(input('Velocidade da espaçonave da SpaceX em quilômetros por hora (km/h): '))
Time_pass = int(input('Tempo passado, em dias, entre o lançamento da SpaceX e Blue Origin: '))
D2_BOrigin = int(input('Distância da trajetória, em quilômetros (km), entre a Terra e Marte no lançamento da Blue Origin: '))
V2_BOrigin = int(input('Velocidade da espaçonave da Blue Origin em quilômetros por hora (km/h): '))

# Cálculo do tempo total gasto por cada espaçonave 
calcular_spaceX = D1_SpaceX / V1_SpaceX
calcular_BOrigin = (D2_BOrigin / V2_BOrigin) + (Time_pass * 24)

if calcular_spaceX < calcular_BOrigin:
    resultado = True
else:
    resultado = False

# Impressão da resposta
print(resultado)

