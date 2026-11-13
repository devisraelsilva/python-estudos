"""Aula 05 (string) — Pedaços de String

Resumo: retirando do texto pedaços de string, por posição de caracteres.
"""

precos = "Jan: R$25,99, Fev: R$32,79, Mar: R$42,99"
preco_jan = precos[5:12]
preco_fev = precos[-21:-14]
preco_mar = precos[-7:]
print(preco_jan)
print(preco_fev)
print(preco_mar)