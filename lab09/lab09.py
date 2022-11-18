###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: FERNANDO CASTRO
# RA: Controle de Estoque 2.0 
###################################################

# Leitura de dados
estoque = {}

def addProdutoEstoque(nomeProduto):
    if nomeProduto not in estoque:
        estoque[nomeProduto] = {'esttoque': 0, 'pedidoCompra': 0, 'pedidoVenda': 0}


def calculadorProdutoEstoque(qtd_produto, nome_produto):
    if qtd_produto < 0:
        if (qtd_produto*-1) <= estoque[nome_produto]['esttoque']:
            estoque[nome_produto]['esttoque'] += qtd_produto
            estoque[nome_produto]['pedidoVenda'] += 1

        else:
            print(f"Quantidade indisponivel para a venda de {qtd_produto*-1} unidade(s) do produto {nome_produto}.")
            if estoque[nome_produto]['esttoque'] <= 0:
                del estoque[nome_produto]
    else:
        estoque[nome_produto]['esttoque'] += qtd_produto
        estoque[nome_produto]['pedidoCompra'] += 1



while True:
    produto = input()

    if produto.lower() == 'fim':
        break

    lista = list(produto.split(" : "))

    addProdutoEstoque(lista[0])
    calculadorProdutoEstoque(int(lista[1]), lista[0])

# Impressão da saída
for i in sorted(estoque):
  print(f"Produto: {i}")
  print(f"Quantidade em Estoque: {estoque[i]['esttoque']}")
  print(f"Pedidos de Compra: {estoque[i]['pedidoCompra']}")
  print(f"Pedidos de Venda: {estoque[i]['pedidoVenda']}")