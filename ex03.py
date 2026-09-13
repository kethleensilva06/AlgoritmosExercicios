# ============================================================
# Exercício 03 - Entrada de dados do usuário (input) + recibo
# ------------------------------------------------------------
# Objetivo: aprender a pedir informações para quem está usando
# o programa (input), converter o texto digitado para números
# (float/int) e montar um recibo formatado, com valores em reais.
# ============================================================


def formatar_em_reais(valor):
    """
    Recebe um número (ex.: 1234.5) e devolve um texto no padrão
    brasileiro de dinheiro (ex.: "1.234,50").

    Não usamos o módulo `locale` do Python porque ele depende de
    configurações do sistema operacional (que podem não existir
    em todo computador) — então fazemos a formatação "na mão":
    1. formatamos com 2 casas decimais e separador de milhar (,)
       no padrão americano, ex.: "1,234.50"
    2. trocamos os símbolos de lugar para o padrão brasileiro
    """
    texto_americano = f"{valor:,.2f}"  # ex.: "1,234.50"
    texto_brasileiro = (
        texto_americano
        .replace(",", "X")   # guarda o separador de milhar num símbolo temporário
        .replace(".", ",")   # o ponto decimal americano vira vírgula
        .replace("X", ".")   # o símbolo temporário vira ponto de milhar
    )
    return texto_brasileiro


# ============ ENTRADA DE DADOS ============
print("=" * 50)
print(" SISTEMA DE COMPRAS")
print("=" * 50)

# input() sempre devolve texto (string), por isso precisamos
# converter manualmente para número quando for o caso.
nome_cliente = input("Nome do cliente: ")
produto = input("Nome do produto: ")
preco = float(input("Preço unitário (R$): "))       # texto -> número decimal
quantidade = int(input("Quantidade: "))               # texto -> número inteiro
percentual_desconto = float(input("Percentual de desconto (%): "))

# ============ PROCESSAMENTO ============
subtotal = preco * quantidade
valor_desconto = subtotal * (percentual_desconto / 100)
total_final = subtotal - valor_desconto
valor_medio = total_final / quantidade  # quanto ficou cada unidade, já com desconto

# ============ SAÍDA FORMATADA ============
print("\n" + "=" * 50)
print(" RECIBO DA COMPRA")
print("=" * 50)

print(f"Cliente: {nome_cliente}")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade} unidade(s)")
print(f"Preço unitário: R$ {formatar_em_reais(preco)}")
print("-" * 50)
print(f"Subtotal: R$ {formatar_em_reais(subtotal)}")
print(f"Desconto: {percentual_desconto:.0f}% (R$ {formatar_em_reais(valor_desconto)})")
print("-" * 50)
print(f"TOTAL A PAGAR: R$ {formatar_em_reais(total_final)}")
print(f"\nValor médio por unidade: R$ {formatar_em_reais(valor_medio)}")

print("\n" + "=" * 50)
print(" OBRIGADO PELA COMPRA!")
print("=" * 50)

# end="..." faz o print não pular linha, permitindo simular uma
# "barra de progresso" simples na mesma linha do texto seguinte.
print("Processando dados", end="... ")
print("Finalizado!", end="\n\n")
