"""Aula 05 (string) — Metodos de string.

Resumo: Alguns metodos essênciais para utilização com Strings.
"""

#Capitalize(): Coloca a primeira letra Maiúscula.
texto = "israel"
print(texto.capitalize())

#Title(): Coloca a primeira letra de cada palavra em Maiúscula.
texto = "israel silva"
print(texto.title())

#Upper(): Coloca o texto todo em Maiúscula.
texto = "israel silva"
print(texto.upper())

#Casefold(): Transforma todas as letras em minúsculas.
texto = "IsRAeL"
print(texto.casefold())

#Count(): Quantidade de vezes que um valor existe na string.
texto = "mafagafo azulado"
print(texto.count("a"))

#Startswith(): Verifica se o texto começa com o valor determinado, com boolean
texto = "israel.silva@gmail.com"
print(texto.startswith("israel"))

#Endswith(): Verifica se o texto termina com o valor determinado, com boolean
texto = "israel.silva@gmail.com"
print(texto.endswith("@gmail.com"))

#Find(): Procura um determinado valor dentro do texto e retorna a posição dela no texto.
texto = "israel@gmail.com"
print(texto.find("@"))

#Isalnum(): Verifica se o texto é feito todo com caracteres alfanuméricos(letras e números).
texto = "Raels97"
print(texto.isalnum())

#Isalpha(): Verifica se são somente letras.
texto = "Rael"
print(texto.isalpha())

#Isnumeric(): Verifica se são somente números.
texto = "1997"
print(texto.isnumeric())

#Replace(): Substitui um determinado valor, por outro a ser declarado. Primeiro argumento será substituído pelo segundo argumento.
texto = "IsRael"
print(texto.replace("s", " "))

#Split(): Separa o texto por um delimitador a declarar.
texto = "israel@gmail.com"
print(texto.split("@"))

#Splitlines(): Separa o texto em vários textos de acordo com o "Enter".
texto = """Aula 05 (string) — Metodos de string
Resumo: 
anote em uma 
ou duas linhas o que a aula ensina.
"""
print(texto.splitlines())

#Strip(): Remove caracteres indesejados do texto, por padrão "spaces" no início e no final.
texto = " 123teste "
print(texto.strip())