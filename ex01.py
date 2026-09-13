# ============================================================
# Exercício 01 - Variáveis, tipos de dados e f-strings
# ------------------------------------------------------------
# Objetivo: entender como o Python guarda valores em variáveis,
# como fazer contas simples e como montar textos que misturam
# palavras com o resultado de variáveis (f-strings).
# ============================================================

# Uma variável é só um "nome" que aponta para um valor guardado
# na memória. Aqui criamos uma variável do tipo string (texto).
linguagem = "Python"
print(linguagem)  # mostra: Python

# O Python também funciona como uma calculadora.
# Ele respeita a ordem das operações matemáticas (multiplicação
# antes da soma), por isso o resultado é 14 e não 20.
resultado_conta = 2 + 3 * 4
print(resultado_conta)  # mostra: 14

# f-string é uma forma de colocar o valor de uma variável dentro
# de um texto. Basta colocar um "f" antes das aspas e escrever
# o nome da variável entre chaves {}.
mensagem = f"Olá, {linguagem}!"
print(mensagem)  # mostra: Olá, Python!

# Podemos guardar a "expressão" (a conta em si, como texto) e o
# "resultado" (o valor calculado) em variáveis separadas...
expressao_em_texto = "2 + 3 * 4"
valor_calculado = 2 + 3 * 4  # o Python calcula e guarda só o número

print(expressao_em_texto)  # mostra: 2 + 3 * 4
print(valor_calculado)     # mostra: 14

# ...e depois juntar as duas coisas em uma única frase.
# Para concatenar (juntar) string com número usando o "+", é
# preciso converter o número para texto primeiro, com str().
frase_concatenada = expressao_em_texto + " = " + str(valor_calculado)
print(frase_concatenada)  # mostra: 2 + 3 * 4 = 14

# A mesma frase só que usando f-string, que é mais legível e não
# precisa da conversão manual com str() — o Python faz isso sozinho.
frase_com_fstring = f"{expressao_em_texto} = {valor_calculado}"
print(frase_com_fstring)  # mostra: 2 + 3 * 4 = 14
