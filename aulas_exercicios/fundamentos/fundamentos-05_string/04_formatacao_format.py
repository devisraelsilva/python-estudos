"""Aula 05 (string) — Formatação.

Resumo: formatações personalizadas para utilizar com o .format.
"""

# :< Alinha o texto à esquerda (se tiver espaço na tela para isso)
# :> Alinha o texto à direita (se tiver espaço na tela para isso)
# :^ Alinha o texto ao centro (se tiver espaço na tela para isso)
# :+ Coloca o sinal sempre na frente do número (independente se é positivo ou negativo)
# :, Coloca a vírgula como separador de milhar
# :_ Coloca o _ como separador de milhar
# :e Formato Científico
# :f Número com quantidade fixa de casas decimais
# :x Formato HEX minúscula (para cores)
# :X Formato HEX maiúscula (para cores)
# :% Formato Percentual

#Exemplo de alinhamento de texto:
texto = "israel@gmail.com"
print("Meu email é diferente de {:<50}.".format(texto)) #Alinha a esquerda, caixa para 50 chars.
print("Meu email é diferente de {:>50}.".format(texto)) #Alinha a direita, caixa para 50 chars.
print("Meu email é diferente de {:^50}.".format(texto)) #Centraliza, caixa para 50 chars.

#Exemplo com valores negativos(-) e positivos(+):
custo = 500
faturamento = 450
lucro = faturamento - custo
print("O faturamento foi de {:+} e o lucro foi de {:+}.".format(faturamento, lucro))

#Exemplo com separador de milhar, com casas decimais e percentual:
custo = 50000
faturamento = 77450
lucro = faturamento - custo
margem = lucro / faturamento
print("O faturamento foi de $ {:+,.2f} e o lucro foi de $ {:+,.2f}. A margem de aumento patrimonial foi de {:.1%}.".format(faturamento, lucro, margem))
#Para transformar os valores em formato brasileiro:
lucro_texto = "R$ {:_.2f}".format(lucro)
print(lucro_texto.replace(".", ","). replace("_", "."))

#Exemplo com arredondamento de número no percent:
imposto = 0.987345
preco = 100
valor_imposto = round(preco * imposto, 2)
print("Imposto a ser pago é de: {}".format(valor_imposto))
