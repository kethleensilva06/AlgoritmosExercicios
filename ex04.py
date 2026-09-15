# Exercicio 04 - if / elif / else
# regra: menor de 16 nao entra, 16+ com ingresso entra, 16+ sem ingresso precisa comprar

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 18:
            print("Acesso negado, não pode ser menor de idade.")
            continue
        break
    except ValueError:
        print("Digite um numero valido.")

while True:
    resposta = input("Voce possui ingresso? (sim/nao): ").strip().lower()
    if resposta in ("sim", "s"):
        tem_ingresso = True
        break
    elif resposta in ("nao", "n"):
        tem_ingresso = False
        break
    else:
        print("Responda com 'sim' ou 'nao'.")

if idade < 16:
    mensagem = "Acesso nao permitido"
elif tem_ingresso:
    mensagem = "Entrada liberada"
else:
    mensagem = "Compre um ingresso"

print("\n" + "=" * 40)
print(f"Idade: {idade} | Ingresso: {'Sim' if tem_ingresso else 'Nao'}")
print(f"Status: {mensagem}")
print("=" * 40)
