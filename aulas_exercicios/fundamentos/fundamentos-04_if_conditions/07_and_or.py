"""Aula 17 — Condicionais com And e Or

Resumo: And e Or.
"""

print("===== Verificação de bônus de funcionário =====\nBônus de 3% para atingimento de meta pessoal e meta firma.*\n")
meta_funcionario = int(input("Qual é a meta do funcionário? "))
qtde_vendas_funcionario = int(input("Quantas vendas foram feitas pelo funcionário? "))
meta_loja = int(input("Qual a meta da loja? "))
qtde_vendas_loja = int(input("Quantas vendas foram feitas na loja? "))


if qtde_vendas_funcionario > meta_funcionario and qtde_vendas_loja > meta_loja:
    bonus = 0.03 * qtde_vendas_funcionario
    print(f"\nBônus do funcionário foi de: R$ {bonus:.2f}")
else:
    print("\nO funcionário não recebeu bônus.")

print("\n===== Rating =====\nRating abaixo de 3: Perde o bônus mesmo batendo a meta.*\nRating acima de 9: Ganha bonus mesmo não batendo a meta.*\n")
rate_funcionario = int(input("Qual o rating do funcionário? "))
rate_meta = 9
rate_cancela = 3

if rate_funcionario <= rate_cancela:
    print("\nDe acordo com a política de rating da empresa, o funcionário perdeu completamente o direito ao bônus.")
elif rate_funcionario >= rate_meta or (qtde_vendas_funcionario > meta_funcionario and qtde_vendas_loja > meta_loja):
    bonus = 0.03 * qtde_vendas_funcionario
    print(f"\nDe acordo com a política de rating da empresa, foi alcançado o bônus ao funcionário de: R$ {bonus:.2f}.")
else:
    print("\nFuncionário não recebeu bônus.")