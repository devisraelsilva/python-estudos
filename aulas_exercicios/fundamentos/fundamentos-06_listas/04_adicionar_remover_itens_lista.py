"""Aula 06 (listas) — Adicionar e Remover itens da Lista

Resumo: anote em uma ou duas linhas o que a aula ensina.
"""

#Adicionar: lista.append(item)
#Remover: lista.pop(indice) / lista.remove(item)

produtos = ["iphone 17", "mac book", "ipad", "airpods"]
print(produtos)

produtos.append("iphone 18")
print(produtos)

item_removido = produtos.pop(0)
print(produtos)
print(f"Atualizamos a lista, removendo o {item_removido} e adicionando o {produtos[3]}.")

produtos.remove("ipad")
print(produtos)