"""Aula 06 (listas) — Introdução listas

Resumo: introdução ao tema de listas.
"""

cargo1 = input("Digite o primeiro cargo: ")
func_cargo1 = input("Quantos funcionários tem no setor {}? ".format(cargo1))
cargo2 = input("\nDigite o segundo cargo: ")
func_cargo2 = input("Quantos funcionários tem no setor {}? ".format(cargo2))
cargo3 = input("\nDigite o terceiro cargo: ")
func_cargo3 = input("Quantos funcionários tem no setor {}? ".format(cargo3))

lista_cargo = [cargo1, cargo2, cargo3]
lista_qtde_func = [func_cargo1, func_cargo2, func_cargo3]

print(lista_cargo)
print("\nImprimindo o segundo item da lista, indice 1.")
print(lista_cargo[1])

print("\n\nNo setor {} existem {} funcionários, no setor {} tem {} funcionários e em {} existem {}.".format(lista_cargo[0], lista_qtde_func[0],lista_cargo[1], lista_qtde_func[1], lista_cargo[2], lista_qtde_func[2]))