print("========== Tabuada ==========\n")
tabuada=int(input("Digite um número para ver a tabuada: "))
print(f"\nTabuada do {tabuada}:\n")

print("========== Resultado ==========\n")
for valor in range(1, 11):
    resultado=tabuada*valor
    print(f"{tabuada} x {valor} = {resultado}")

print("\nFim do programa.")