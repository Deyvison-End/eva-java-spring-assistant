import ollama
from pathlib import Path

def ler_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def carregar_conhecimento(caminho):
    arquivos = Path(caminho).rglob("*.md")
    conhecimento = ""

    for arquivo in arquivos:
        conhecimento += ler_arquivo(arquivo) + "\n\n"

    return conhecimento

resposta = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": ler_arquivo("prompts/system.md")
        },
        {
            "role": "system",
             "content": carregar_conhecimento("data")
               
        },            
        {
            "role": "user",
            "content": input("Digite sua dúvida: ")
        }
        ]
        
)

print(resposta["message"]["content"])