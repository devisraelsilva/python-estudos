print("========== Dados do paciente ==========")
nome=input("\nDigite seu nome: ")
idade=int(input("Digite sua idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()

print("\n========== Resultado da avaliação ==========\n")

if idade >= 65:
    print(f"{nome}, você possui atendimento prioritário.")
elif doenca_infectocontagiosa == "SIM":
    print(f"{nome}, você possui suspeita de doença infectocontagiosa e deve ser atendido(a) em uma sala isolada.")
else:
    print(f"{nome}, você não possui atendimento prioritário, aguardar atendimento em uma sala comum.")

print("\n\nFim do programa.")