import ollama
import string
from pathlib import Path

stopwords = ["o", "a", "os", "as", "que", "é", "de", "do", "da", "em", "um", "uma"]

def tirar_caracteres_especiais(palavras):
    palavras_limpa = []

    for palavra in palavras:
        palavra = palavra.strip(string.punctuation)
        palavras_limpa.append(palavra)

    return palavras_limpa


def buscar_conhecimento(pergunta, caminho):
    palavras = pergunta.lower().split()

    palavras = tirar_caracteres_especiais(palavras)

    palavras_chave = []

    for palavra in palavras:
        if palavra not in stopwords:
            palavras_chave.append(palavra)


    resultados = {}

    arquivos = Path(caminho).rglob("*.md")

    for arquivo in arquivos:
        conteudo = ler_arquivo(arquivo).lower()

        pontuacao = 0

        for palavra in palavras_chave:
            pontuacao += conteudo.count(palavra)

        resultados[arquivo] = pontuacao

    return resultados


def ler_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def carregar_conhecimento(caminho):
    arquivos = Path(caminho).rglob("*.md")
    conhecimento = ""

    for arquivo in arquivos:
        conhecimento += ler_arquivo(arquivo) + "\n\n"

    return conhecimento


def main():
    prompt_base = ler_arquivo("prompts/system.md")

    mensagens = [
        {
            "role": "system",
            "content": prompt_base
        }
    ]

    print("Eva: Olá! Sou a Eva, sua assistente de Java e Spring Boot.")
    print("Digite 'sair' para encerrar a conversa.\n")

    while True:
        pergunta = input("Você: ").strip()

        if pergunta.lower() == "sair":
            print("Eva: Até a próxima!")
            break

        if not pergunta:
            continue

        resultados = buscar_conhecimento(pergunta, "data")

        ordenados = sorted(
            resultados.items(),
            key=lambda item: item[1],
            reverse=True
        )

        top_3 = [
            (arquivo, pontuacao)
            for arquivo, pontuacao in ordenados
            if pontuacao > 0
        ][:3]

        conhecimento_relevante = ""

        for arquivo, pontuacao in top_3:
            conhecimento_relevante += (
                f"\n### Documento: {arquivo.name}\n"
                f"{ler_arquivo(arquivo)}\n"
            )

        pergunta_com_contexto = pergunta

        if conhecimento_relevante.strip():
            pergunta_com_contexto = f"""
### BASE DE CONHECIMENTO
{conhecimento_relevante}

### PERGUNTA DO ESTUDANTE
{pergunta}
"""

        mensagens.append({
            "role": "user",
            "content": pergunta_com_contexto
        })

        try:
            resposta = ollama.chat(
                model="qwen3:8b",
                messages=mensagens
            )

            conteudo_resposta = resposta["message"]["content"]

            print(f"\nEva: {conteudo_resposta}\n")

            mensagens.append({
                "role": "assistant",
                "content": conteudo_resposta
            })

        except Exception as erro:
            print(f"\nErro ao consultar o modelo: {erro}\n")
            mensagens.pop()


if __name__ == "__main__":
    main()
    