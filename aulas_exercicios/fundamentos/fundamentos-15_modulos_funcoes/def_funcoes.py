def preencherInventario(lista):
    resposta="S"
    while resposta=="S":
        equipamento=[input("Equipamento: "), float(input("Valor: ")), int(input("Número Serial: ")), input("Departamento: ")]
        lista.append(equipamento)
        resposta=input("Digite \"S\" para continuar...").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])

def localizarPorNome(lista, nome):
    encontrado=False
    for elemento in lista:
        if nome==elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.: ", elemento[2])
            encontrado=True

    if not encontrado:
        print("Equipamento \"{}\" não encontrado.".format(nome))

def depreciarPorNome(lista, nome, percentual):
    encontrado=False
    for elemento in lista:
        if nome==elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1 - percentual/100)
            print("Novo valor: ", elemento[1])
            encontrado=True

    if not encontrado:
        print("Equipamento \"{}\" não encontrado.".format(nome))

def excluirPorSerial(lista, serial):
    encontrado=False
    for elemento in lista:
        if elemento[2]==serial:
            lista.remove(elemento)
            print("Equipamento \"{}\", excluído.".format(elemento[0]))
            encontrado=True
            break

    if not encontrado:
        print("Equipamento com serial \"{}\" não encontrado.".format(serial))

def resumirValores(lista):
    valores=[]
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores)>0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))