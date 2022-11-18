##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: FERNANDO CASTRO
# RA: Jornada de Trabalho
##################################################

# Leitura do valor da hora
valorHora = int(input())

# Leitura do numero de dias trabalhados na semana
numeroDias = int(input())

# Leitora e processamento dos periodos de trabalho de cada dia
horas_trabalhadas = 0
horas_extras = 0
for numero in range(0,numeroDias):
    calcularHoraExtra = 0
    numeroPeriodos = int(input())
    for num in range(0, numeroPeriodos):
        inicioPeriodo = int(input())
        fimPeriodo = int(input())
        calcularHoraExtra +=  fimPeriodo - inicioPeriodo

    if calcularHoraExtra > 8:
        horas_extras += (calcularHoraExtra - 8)
    horas_trabalhadas += calcularHoraExtra

# Calculo do valor devido ao funcionário

if (horas_trabalhadas - horas_extras) > 44:
    horas_extras += ((horas_trabalhadas - 44 ) - horas_extras)
valor = ( horas_trabalhadas * valorHora ) + ((horas_extras * valorHora) * 0.5)

# Impressão da saída
print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))