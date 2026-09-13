# ============================================================
# Exercício 04 - Estruturas condicionais (if / elif / else)
# ------------------------------------------------------------
# Programa: Classificador de acesso a um evento
# Regras:
#   - Menor de 16 anos          -> acesso negado
#   - 16 anos ou mais COM ingresso -> entrada liberada
#   - 16 anos ou mais SEM ingresso -> precisa comprar ingresso
#
# Objetivo: aprender a validar entradas do usuário com laços
# `while` + `try/except`, e a tomar decisões com `if/elif/else`.
# ============================================================

# ============ ENTRADA DE DADOS (com validação) ============

# Usamos um "while True" (loop infinito) que só é interrompido
# pelo "break" quando o usuário digita um valor válido.
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            # idade negativa não faz sentido: avisa e pede de novo
            print("Idade não pode ser negativa. Tente novamente.")
            continue  # volta para o início do while, sem passar pelo break
        break  # idade válida: sai do loop
    except ValueError:
        # int() falha se o usuário digitar algo que não é número
        # (ex.: "abc"); capturamos o erro para não travar o programa
        print("Entrada inválida! Digite um número inteiro para a idade.")

# Mesma lógica de validação, mas para uma pergunta de sim/não.
while True:
    resposta = input("Você possui ingresso? (sim/nao): ").strip().lower()
    if resposta in ("sim", "s"):
        tem_ingresso = True
        break
    elif resposta in ("nao", "não", "n"):
        tem_ingresso = False
        break
    else:
        print("Resposta inválida! Digite 'sim' ou 'nao'.")

# ============ PROCESSAMENTO (tomada de decisão) ============

# if / elif / else são avaliados em ordem, de cima para baixo.
# Assim que uma condição é verdadeira, o Python executa aquele
# bloco e ignora todos os outros.
if idade < 16:
    # Caso 1: não importa se tem ingresso, é menor de idade
    mensagem = "Acesso não permitido"
    status = "negado"
elif tem_ingresso:
    # Caso 2: aqui já sabemos que idade >= 16 (senão teria caído
    # no "if" acima), então só falta checar o ingresso
    mensagem = "Entrada liberada"
    status = "permitido"
else:
    # Caso 3: sobrou só esta possibilidade -> idade >= 16 e sem ingresso
    mensagem = "Compre um ingresso"
    status = "pendente"

# ============ SAÍDA FORMATADA ============
print("\n" + "=" * 50)
print(" RESULTADO DA CLASSIFICAÇÃO")
print("=" * 50)
print(f"Idade informada: {idade} anos")
print(f"Possui ingresso: {'Sim' if tem_ingresso else 'Não'}")
print("-" * 50)
print(f"Status: {mensagem.upper()}")

# Um segundo if/elif/else só para explicar o motivo, usando a
# variável "status" que guardamos no bloco anterior.
if status == "negado":
    print("Motivo: idade mínima para acesso é 16 anos.")
elif status == "permitido":
    print("Motivo: idade e ingresso verificados com sucesso.")
else:
    print("Motivo: é necessário adquirir um ingresso para entrar.")
print("=" * 50)
