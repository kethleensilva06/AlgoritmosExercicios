# Exercicio 02 - carrinho de compras

titulo = "Calculo no carrinho de compras"
produto = "caderno"
preco = 35.00
quantidade = 2
desconto = 10.00

subtotal = preco * quantidade
total = subtotal - desconto

# :.2f deixa o numero sempre com 2 casas decimais, tipo preco de verdade
print(f"""
{titulo}
Produto: {produto}
Comprou {quantidade} unidades a R$ {preco:.2f} cada
Desconto: R$ {desconto:.2f}

Subtotal: R$ {subtotal:.2f}
Total pago: R$ {total:.2f}
""")
