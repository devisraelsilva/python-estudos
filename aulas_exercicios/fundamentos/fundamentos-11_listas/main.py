print("========== Inventário ==========\n")
inventario = []
resposta = "S"

while resposta == "S":
    inventario.append(input("Digite o nome do item: "))
    inventario.append(float(input("Digite o valor do item: ")))
    inventario.append(int(input("Serial Number do item: ")))
    inventario.append(input("Digite o departamento do item: "))
    resposta = input("\nDigite \"S\" para continuar...\n").upper()

for elemento in inventario:
    print(elemento)