import tiktoken

# Tabela de preços por 1000 tokens (valores de exemplo, atualize conforme necessário)
PRICES = {
    "gpt-3.5-turbo": {
        "input": 0.0015,  # USD por 1K tokens de input
        "output": 0.0020  # USD por 1K tokens de output
    },
    "gpt-4": {
        "input": 0.03,
        "output": 0.06
    }
}

# Multiplicadores para estimar o tamanho da resposta
RESPONSE_SIZE_MULTIPLIER = {
    "curta": 0.5,  # metade do tamanho do input
    "média": 1.0,  # mesmo tamanho do input
    "longa": 2.0   # o dobro do input
}

def calcular_tokens(texto, modelo="gpt-3.5-turbo"):
    encoding = tiktoken.encoding_for_model(modelo)
    tokens = encoding.encode(texto)
    return len(tokens)

def estimar_custo(num_tokens, modelo="gpt-3.5-turbo", tipo="input"):
    preco_por_mil = PRICES[modelo][tipo]
    custo = (num_tokens / 1000) * preco_por_mil
    return custo

def escolher_tamanho_resposta():
    while True:
        tamanho = input("\nQue tamanho de resposta você espera? (curta/média/longa): ").strip().lower()
        if tamanho in RESPONSE_SIZE_MULTIPLIER:
            return tamanho
        print("\nOpção inválida. Por favor, digite uma das opções válidas: [curta] [média] [longa].")

def main():
    print("==== Calculadora de Tokens e Custo para LLMs ====\n")
    
    modelo = input("Escolha o modelo (gpt-3.5-turbo / gpt-4): ").strip()
    if modelo not in PRICES:
        print("Modelo inválido. Usando gpt-3.5-turbo como padrão.")
        modelo = "gpt-3.5-turbo"

    texto = input("\nCole seu texto aqui:\n")
    num_tokens_input = calcular_tokens(texto, modelo)

    tamanho_resposta = escolher_tamanho_resposta()
    multiplicador = RESPONSE_SIZE_MULTIPLIER[tamanho_resposta]
    num_tokens_output_estimado = int(num_tokens_input * multiplicador)

    custo_input = estimar_custo(num_tokens_input, modelo, tipo="input")
    custo_output = estimar_custo(num_tokens_output_estimado, modelo, tipo="output")
    custo_total = custo_input + custo_output

    print("\n===== Resultado =====")
    print(f"Tokens do INPUT: {num_tokens_input} tokens")
    print(f"Tokens do OUTPUT (estimado): {num_tokens_output_estimado} tokens")
    print(f"\nCusto estimado:")
    print(f"- INPUT: ${custo_input:.6f} USD")
    print(f"- OUTPUT: ${custo_output:.6f} USD")
    print(f"- TOTAL: ${custo_total:.6f} USD")
    print("======================")

if __name__ == "__main__":
    main()
