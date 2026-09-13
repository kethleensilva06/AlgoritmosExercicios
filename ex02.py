# ============================================================
# Exercício 02 - Cálculo de compras + formatação de texto
# ------------------------------------------------------------
# Objetivo: usar variáveis para montar um pequeno "recibo",
# fazer contas com desconto e formatar números com casas
# decimais fixas, imprimindo tudo em um texto de várias linhas.
# ============================================================

# --- Dados de entrada (fixos, "cadastrados" no próprio código) ---
titulo = "Cálculo no carrinho de compras"
nome_produto = "caderno"
preco_unitario = 35.00   # preço de cada unidade, em reais
quantidade = 2            # quantas unidades foram compradas
desconto = 10.00          # desconto total dado na compra, em reais

# --- Processamento: as contas em si ---
# Subtotal = preço de uma unidade vezes a quantidade comprada
subtotal = preco_unitario * quantidade

# Valor final = subtotal menos o desconto aplicado
valor_final = subtotal - desconto

# --- Saída formatada ---
# ":.2f" dentro das chaves de uma f-string diz ao Python:
# "mostre este número com exatamente 2 casas decimais"
# (isso evita algo como 60.0 e garante 60.00, como um preço real).
print(f"""
{titulo}
Produto: {nome_produto}
O cliente comprou {quantidade} unidade(s), cada uma por: R$ {preco_unitario:.2f}
Desconto aplicado: R$ {desconto:.2f}

Subtotal (preço x quantidade): R$ {subtotal:.2f}
Quanto ele gastou no total? R$ {valor_final:.2f}
""")
