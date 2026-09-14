# Exercicio 03 - pedindo dados pro usuario e montando um recibo

def formatar_real(valor):
    # troca o ponto e a virgula pra ficar no formato brasileiro (1.234,56)
    texto = f"{valor:,.2f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


print("=" * 50)
print(" SISTEMA DE COMPRAS")
print("=" * 50)

nome_cliente = input("Nome do cliente: ")
produto = input("Nome do produto: ")
preco = float(input("Preco unitario (R$): "))
quantidade = int(input("Quantidade: "))
desconto_pct = float(input("Percentual de desconto (%): "))

subtotal = preco * quantidade
valor_desconto = subtotal * (desconto_pct / 100)
total = subtotal - valor_desconto
valor_medio = total / quantidade

print("\n" + "=" * 50)
print(" RECIBO DA COMPRA")
print("=" * 50)
print(f"Cliente: {nome_cliente}")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade} unidade(s)")
print(f"Preco unitario: R$ {formatar_real(preco)}")
print("-" * 50)
print(f"Subtotal: R$ {formatar_real(subtotal)}")
print(f"Desconto: {desconto_pct:.0f}% (R$ {formatar_real(valor_desconto)})")
print("-" * 50)
print(f"TOTAL A PAGAR: R$ {formatar_real(total)}")
print(f"Valor medio por unidade: R$ {formatar_real(valor_medio)}")
print("=" * 50)
