# ============================================================
# Exercício 05 - Estruturas de seleção avançadas
# ------------------------------------------------------------
# Sistema simples de notas escolares, mostrando 4 jeitos
# diferentes de tomar decisões em Python:
#   1) if aninhado        (um if dentro de outro if)
#   2) if / elif encadeado (várias condições em sequência)
#   3) match / case        (parecido com "switch" de outras linguagens)
#   4) match / case com "guarda" (condição extra dentro do case)
# ============================================================


def verificar_aprovacao():
    """
    1) IF ANINHADO: o segundo "if" só é avaliado se o primeiro
    já foi verdadeiro. Isso representa bem uma regra do tipo
    "só verifico a nota SE a frequência já estiver OK".
    """
    print("\n=== VERIFICAÇÃO DE APROVAÇÃO (if aninhado) ===")
    nota = float(input("Nota do aluno (0 a 10): "))
    frequencia = float(input("Frequência do aluno (0 a 100): "))

    if frequencia >= 75:
        # só entramos aqui dentro se a frequência já é suficiente
        print("Frequência OK.")
        if nota >= 7.0:
            print(f"RESULTADO: APROVADO (nota {nota}, frequência {frequencia}%)")
        else:
            print(f"RESULTADO: REPROVADO por nota (nota {nota} < 7.0)")
    else:
        # se a frequência já falhou, nem chegamos a olhar a nota
        print(f"RESULTADO: REPROVADO por frequência ({frequencia}% < 75%)")


def classificar_nota():
    """
    2) IF / ELIF ENCADEADO: as condições são testadas em ordem,
    do caso mais "alto" para o mais "baixo". Assim que uma bate,
    as próximas nem são checadas.
    """
    print("\n=== CLASSIFICAÇÃO DE NOTA (elif encadeado) ===")
    nota = float(input("Nota para classificar (0 a 10): "))

    if nota >= 9.0:
        classificacao = "EXCELENTE"
    elif nota >= 7.0:
        classificacao = "BOM"
    elif nota >= 5.0:
        classificacao = "REGULAR"
    else:
        classificacao = "INSUFICIENTE"

    print(f"Nota {nota} -> CLASSIFICAÇÃO: {classificacao}")


def processar_menu():
    """
    3) MATCH / CASE simples: compara o valor de "opcao" com cada
    padrão (case), na ordem em que aparecem. É uma alternativa
    mais legível a um "elif" gigante quando comparamos um único
    valor com várias opções fixas.
    """
    print("\n=== PROCESSAR MENU (match/case) ===")
    print("1 - Listar alunos | 2 - Cadastrar aluno | 3 - Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("Listando alunos...")
        case "2":
            print("Cadastrando aluno...")
        case "3" | "sair":
            # o "|" permite casar mais de um valor no mesmo case
            print("Saindo do menu...")
        case _:
            # "_" é o "coringa": cai aqui quando nada acima combinou
            print(f"Opção inválida: {opcao}")


def avaliar_aluno():
    """
    4) MATCH / CASE COM GUARDA: cada "case" pode ter uma condição
    extra depois de "if". O Python só considera aquele case como
    combinado se, além do formato bater, a condição também for
    verdadeira. Isso permite decisões mais ricas que um match
    comum, parecido com um if/elif só que comparando uma tupla.
    """
    print("\n=== AVALIAÇÃO DO ALUNO (match/case com guarda) ===")
    nome = input("Nome do aluno: ")
    nota = float(input("Nota (0 a 10): "))
    faltas = int(input("Número de faltas: "))

    dados = (nota, faltas)  # agrupamos os dois valores numa tupla

    match dados:
        case (n, _) if n >= 9.0:
            # o "_" no lugar das faltas significa "não importa esse valor aqui"
            print(f"{nome}: ALUNO DESTAQUE (nota {n})")
        case (n, f) if n >= 7.0 and f <= 10:
            print(f"{nome}: APROVADO (nota {n}, faltas {f})")
        case (n, f) if n >= 5.0 and f <= 10:
            print(f"{nome}: EM RECUPERAÇÃO (nota {n}, faltas {f})")
        case _:
            print(f"{nome}: REPROVADO (nota {nota}, faltas {faltas})")


def main():
    """Menu interativo que dá acesso às quatro demonstrações acima."""
    opcoes = {
        "1": verificar_aprovacao,
        "2": classificar_nota,
        "3": processar_menu,
        "4": avaliar_aluno,
    }

    while True:
        print("\n" + "=" * 50)
        print("SISTEMA ESCOLAR - ESTRUTURAS DE SELEÇÃO")
        print("=" * 50)
        print("1 - Verificar Aprovação (if aninhado)")
        print("2 - Classificar Nota (if/elif)")
        print("3 - Processar Menu (match/case)")
        print("4 - Avaliar Aluno (match/case com guarda)")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == "5":
            print("Saindo do sistema...")
            break
        elif opcao in opcoes:
            # busca a função correspondente no dicionário "opcoes"
            # e a executa (o "()" no final é o que chama a função)
            opcoes[opcao]()
        else:
            print("Opção inválida! Tente novamente.")


# Este "if" garante que main() só roda quando o arquivo é
# executado diretamente (python ex05.py), e não quando ele é
# apenas importado por outro script.
if __name__ == "__main__":
    main()
