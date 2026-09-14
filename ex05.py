# Exercicio 05 - formas de tomar decisao em Python
# if aninhado, if/elif encadeado, match/case e match/case com guarda

def verificar_aprovacao():
    print("\n-- Verificar aprovacao (if aninhado) --")
    nota = float(input("Nota (0 a 10): "))
    frequencia = float(input("Frequencia (0 a 100): "))

    if frequencia >= 75:
        if nota >= 7.0:
            print("Aprovado")
        else:
            print("Reprovado por nota")
    else:
        print("Reprovado por frequencia")


def classificar_nota():
    print("\n-- Classificar nota (if/elif) --")
    nota = float(input("Nota (0 a 10): "))

    if nota >= 9.0:
        print("Excelente")
    elif nota >= 7.0:
        print("Bom")
    elif nota >= 5.0:
        print("Regular")
    else:
        print("Insuficiente")


def processar_menu():
    print("\n-- Menu (match/case) --")
    print("1 - Listar | 2 - Cadastrar | 3 - Sair")
    opcao = input("Opcao: ")

    match opcao:
        case "1":
            print("Listando alunos...")
        case "2":
            print("Cadastrando aluno...")
        case "3":
            print("Saindo...")
        case _:
            print("Opcao invalida")


def avaliar_aluno():
    print("\n-- Avaliar aluno (match/case com guarda) --")
    nome = input("Nome: ")
    nota = float(input("Nota (0 a 10): "))
    faltas = int(input("Faltas: "))

    match (nota, faltas):
        case (n, _) if n >= 9.0:
            print(f"{nome}: destaque")
        case (n, f) if n >= 7.0 and f <= 10:
            print(f"{nome}: aprovado")
        case (n, f) if n >= 5.0 and f <= 10:
            print(f"{nome}: recuperacao")
        case _:
            print(f"{nome}: reprovado")


def main():
    opcoes = {
        "1": verificar_aprovacao,
        "2": classificar_nota,
        "3": processar_menu,
        "4": avaliar_aluno,
    }

    while True:
        print("\n1-Aprovacao  2-Classificar  3-Menu  4-Avaliar  5-Sair")
        opcao = input("Escolha: ")

        if opcao == "5":
            break
        elif opcao in opcoes:
            opcoes[opcao]()
        else:
            print("Opcao invalida")


if __name__ == "__main__":
    main()
