nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))

if idade >= 65:
    print(f"\n{nome}, você é idoso(a) e possui atendimento prioritário.")
else:
    print(f"{nome}, você não possui atendimento prioritário.")

print("\nFim do programa.")