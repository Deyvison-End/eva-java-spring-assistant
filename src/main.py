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

    pergunta = input("Digite sua dúvida: ")

    resultados = buscar_conhecimento(pergunta, "data")

    ordenados = sorted(
        resultados.items(),
        key=lambda item: item[1],
        reverse=True
    )

    top_3 = ordenados[:3]

    conhecimento_relevante = ""

    for arquivo, pontuacao in top_3:
        if pontuacao > 0:
            conhecimento_relevante += ler_arquivo(arquivo) + "\n\n"

    

    prompt_base += """

        ## Base de conhecimento

        Use o conteúdo abaixo como fonte de conhecimento para responder à pergunta.
        Priorize essas informações e não invente informações que não estejam presentes
        na base quando a pergunta depender dela.

        """ + "\n\n" + conhecimento_relevante

    resposta = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": prompt_base
            },
            {
                "role": "user",
                "content": pergunta
            }
        ]
    )

    print(resposta["message"]["content"])

if __name__ == "__main__":
    main()