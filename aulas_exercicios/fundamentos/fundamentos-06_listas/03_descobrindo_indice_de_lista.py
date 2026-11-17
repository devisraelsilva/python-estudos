"""Aula 06 (listas) — Descobrindo indice de lista

Resumo: Descobrindo o Índice de um item na lista
"""

produtos = ["hd", "ram", "fonte", "cpu", "gpu"]
estoque = [12, 7, 9, 4, 2]

produto_procurado = input("Qual produto precisa saber a quantidade do estoque?\n(HD, RAM, Fonte, CPU ou GPU)\n").lower()

if produto_procurado in produtos:
    i = produtos.index(produto_procurado)
    qtde_estoque = estoque[i]
    
    print(f"\nEste produto é o indice numero {i}.")
    print(f"Somente para conferência, o indice acima é do produto {produtos[i]}.")
    print(f"A quantidade em estoque deste produto é de {qtde_estoque} unidades.")
else:
    print("Produto informado não existe, favor verificar.")