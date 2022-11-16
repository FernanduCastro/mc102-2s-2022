###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: FERNANDO CASTRO
# RA: YOU SHALL NOT PASS
###################################################

listaPalavra = []
listaTentativas = []
contagem = 0

# Leitura da palavra
palavra = str(input()).lower().strip()

for i in palavra:
    listaPalavra.append(i)


while True:
# Resetador da lista e contador das tentativas
    listaTentativas.clear()
    confirmadorDeLetra = 0

# Impressão da linha final se acertar a resposta
    if contagem == 6:
        print(f'Palavra correta: {palavra}')
        break
    
# Leitura dos palpites e impressão do resultado para cada palpite
    tentativas = str(input()).lower().strip()

    for letra in tentativas:
        listaTentativas.append(letra)
        if listaPalavra[confirmadorDeLetra] == letra:
            print(letra.upper(), end="")
        else:
            if letra in listaPalavra:
                print(letra, end="")
            else:
                letra = '_'
                print(letra, end="")

        confirmadorDeLetra +=1

    print('\n', end="")

    contagem += 1
# Impressão da linha final se a reposta for correta
    if tentativas == palavra:
        print('Resposta correta')
        break
