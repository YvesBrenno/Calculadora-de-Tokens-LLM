
# Calculadora de Tokens para LLM

Ferramenta simples em Python para calcular a quantidade de tokens de um texto e estimar o custo de interagir com modelos de linguagem como o GPT-3.5 ou GPT-4.

## Sobre o Projeto

Esse projeto faz parte de um estudo sobre LLMs visando:
- Compreender funcionam os tokens em Large Language Models (LLMs).
- Calcular quantos tokens um texto consome.
- Estimar o custo de uso com base na tabela de preços de API (OpenAI, etc).

Foram utilizadas bibliotecas oficiais e reconhecidas no mercado, como tiktoken, para garantir melhor precisão.

## Funcionalidades
- Conta quantos tokens um texto possui.
- Estima o custo de envio (input) do texto.
- Estima o custo de resposta (output) baseado em tamanho esperado.
- Permite escolher o modelo (gpt-3.5-turbo ou gpt-4).
- Permite escolher o tamanho esperado da resposta (curta, média ou longa).

## Tabela de Preços Utilizados (exemplo)

| Modelo           | Preço Input (por 1K tokens) | Preço Output (por 1K tokens) |
|:-----------------|:-----------------------------|:------------------------------|
| GPT-3.5-Turbo    | $0.0015 USD                   | $0.0020 USD                   |
| GPT-4            | $0.0300 USD                   | $0.0600 USD                   |

*(Esses valores podem mudar. Atualize se necessário.)*

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/YvesBrenno/Calculadora-de-Tokens-LLM.git 
```

2. Instale as dependências:
```bash
pip install tiktoken
```

3. Execute o programa:
```bash
python calculadora.py
```

## Como Usar

- Escolha o modelo de linguagem.
- Cole o texto que deseja analisar.
- Escolha o tamanho esperado da resposta:
  - Curta (~50% do tamanho do prompt)
  - Média (~100% do tamanho do prompt)
  - Longa (~200% do tamanho do prompt)
- Veja o número de tokens e o custo estimado!

## Observação Importante
- O custo do **input** é calculado exatamente com base no texto enviado.
- O custo do **output** é **estimado** baseado no tamanho esperado da resposta, pois não é possível saber a resposta antes de recebê-la.
