"""Aula 18 — Comparações Contraintuitivas
Resumo: Comparações que não utilizam os comparadores lógicos.
"""

faturamento = input("\nQual foi o faturamento da loja nesse mês? ")
custo = input("Qual foi o custo da loja nesse mês? ")

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print(f"O lucro da loja foi de R$ {lucro:.2f} reais.")
else:
    print("Preencha corretamente o faturamento e o lucro!")



#Comparações contraintuitivas mais frequêntes são:
#IF 0:
#IF ":