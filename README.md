# Algoritmos Exercícios (refeitos)

Este repositório recria os exercícios 1 a 5 do repositório original
[`profedsonvieira/AlgoritmosExercicios`](https://github.com/profedsonvieira/AlgoritmosExercicios),
com implementação própria e **comentários explicando cada trecho do código**.
A ideia é servir como material de estudo para quem está aprendendo lógica de
programação e Python básico.

## Como rodar

Basta ter Python 3.10+ instalado (necessário por causa do `match/case` usado
no exercício 5) e executar cada arquivo separadamente:

```bash
python3 ex01.py
python3 ex02.py
python3 ex03.py   # pede dados pelo teclado
python3 ex04.py   # pede dados pelo teclado
python3 ex05.py   # menu interativo, pede dados pelo teclado
```

## Exercícios

### `ex01.py` — Variáveis, tipos e f-strings
Introduz variáveis, operações aritméticas simples e a diferença entre
concatenar strings com `+` (precisa de `str()`) e usar f-strings (mais
direto). Não pede nada do usuário, só imprime resultados.

### `ex02.py` — Cálculo de compras com texto formatado
Usa variáveis fixas para simular a compra de um produto, calcula subtotal e
valor final com desconto, e imprime um "recibo" em um bloco de texto de
várias linhas (`"""..."""`), usando `:.2f` para garantir sempre 2 casas
decimais nos valores em reais.

### `ex03.py` — Entrada de dados do usuário + recibo formatado
Já pede as informações da compra pelo teclado (`input()`), convertendo texto
para número com `float()`/`int()`. Inclui uma função própria
`formatar_em_reais()` que formata números no padrão brasileiro (ex.:
`1.234,56`) sem depender do módulo `locale` do sistema operacional.

### `ex04.py` — Estruturas condicionais (`if` / `elif` / `else`)
Um classificador de acesso a um evento: pergunta a idade e se a pessoa tem
ingresso, valida as respostas em loops `while` com `try/except`, e decide o
resultado com `if/elif/else`, cobrindo os três cenários possíveis (menor de
idade, maior com ingresso, maior sem ingresso).

### `ex05.py` — Estruturas de seleção avançadas
Um mini sistema escolar com menu interativo que demonstra quatro formas de
tomar decisões em Python:
1. **`if` aninhado** — um `if` dentro do outro (aprovação por nota e frequência).
2. **`if`/`elif` encadeado** — classificação de nota em faixas (EXCELENTE, BOM, etc).
3. **`match`/`case`** — como uma alternativa mais legível a vários `elif` iguais.
4. **`match`/`case` com guarda** — `case` com uma condição `if` extra, permitindo
   regras mais ricas (nota + faltas juntas).

## Diferenças em relação ao repositório original

O código foi reescrito (não copiado) para reforçar o aprendizado, mantendo os
mesmos objetivos didáticos de cada exercício. Foram adicionados comentários
linha a linha, e o exercício 3 usa uma formatação de moeda manual em vez do
módulo `locale`, para funcionar em qualquer computador sem configuração
regional prévia.
