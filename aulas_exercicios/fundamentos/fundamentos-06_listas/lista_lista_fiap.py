inventario=[]
resposta="S"

while resposta=="S":
    equipamento=[input("Equipamento: "), float(input("Valor: ")), int(input("Número Serial: ")), input("Departamento: ")]
    inventario.append(equipamento)
    resposta=input("Digite \"S\" para continuar...").upper()

for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

busca=input("\nDigite o nome do equipamento que deseja buscar: ")
encontrado=False

for elemento in inventario:
    if busca==elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.: ", elemento[2])
        encontrado=True

if not encontrado:
    print("Equipamento \"{}\" não encontrado.".format(busca))

depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
encontrado=False

for elemento in inventario:
    if depreciacao==elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])
        encontrado=True

if not encontrado:
    print("Equipamento \"{}\" não encontrado.".format(depreciacao))

serial=int(input("\nDigite o serial do equipamento que será excluído: "))
encontrado=False
for elemento in inventario:
    if elemento[2]==serial:
        inventario.remove(elemento)
        print("Equipamento \"{}\", excluído.".format(serial))
        encontrado=True

if not encontrado:
        print("Equipamento com serial \"{}\" não encontrado.".format(serial))

for elemento in inventario:
    print("\nNome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

valores=[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))