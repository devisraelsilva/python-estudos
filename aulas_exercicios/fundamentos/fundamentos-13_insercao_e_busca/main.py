print("\n===== Dados fornecidos =====")
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("\nEquipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("\nDigite \"S\" para continuar: ").upper()

busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("\nValor: ", valores[indice])
        print("Número Serial: ", seriais[indice])
        print("O equipamento está localizado no departamento: ", departamentos[indice])
    elif busca not in equipamentos:
        print("\nEquipamento não encontrado.")