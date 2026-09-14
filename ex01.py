# Exercicio 01 - variaveis e f-strings

nome = "Python"
print(nome)

# a multiplicacao acontece antes da soma, entao da 14 e nao 20
conta = 2 + 3 * 4
print(conta)

mensagem = f"Ola, {nome}!"
print(mensagem)

texto = "2 + 3 * 4"
resultado = 2 + 3 * 4

print(texto)
print(resultado)

# pra juntar string com numero usando +, precisa converter com str()
expressao = texto + " = " + str(resultado)
print(expressao)

# com f-string fica mais simples, nao precisa converter nada
expressao2 = f"{texto} = {resultado}"
print(expressao2)
