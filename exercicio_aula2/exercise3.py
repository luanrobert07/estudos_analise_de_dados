dadosAlunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para terminar): ")
    if nome.lower() == 'sair':
        break

    while True:
        try:
            media = float(input(f"Digite a média para {nome}: "))
            break
        except ValueError:
            print("Média inválida. Por favor, insira um número.")

    situacao_final = 'RP' if media < 60 else 'AP'
    dadosAlunos[nome] = [media, situacao_final]

print("\nDicionário final:")
print(dadosAlunos)
