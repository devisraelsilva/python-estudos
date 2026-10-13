from def_funcoes import *

minhaLista=[]
print("\nPreenchendo...")
preencherInventario(minhaLista)
print("\nExibindo...")
exibirInventario(minhaLista)

print("\nPesquisando...")
nome=input("Digite o nome do equipamento que deseja localizar: ")
localizarPorNome(minhaLista, nome)

print("\nAlterando...")
nome=input("Digite o nome do equipamento que será depreciado: ")
depreciarPorNome(minhaLista, nome, 20)

print("\nExcluindo...")
serial=int(input("Digite o número serial do equipamento que deseja excluir: "))
excluirPorSerial(minhaLista, serial)
exibirInventario(minhaLista)

print("\nResumindo...")
resumirValores(minhaLista)