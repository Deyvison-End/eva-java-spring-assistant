import ollama
from pathlib import Path


with open("data/java/coesao-e-acoplamento.md", "r", encoding="utf-8") as coesao_acoplamento:
    coesao_acoplamento = coesao_acoplamento.read()

with open("data/java/poo.md", "r", encoding="utf-8") as poo:
    poo = poo.read()

with open("data/spring-boot/api-rest.md", "r", encoding="utf-8") as api_rest: 
    api_rest = api_rest.read()

with open("data/spring-boot/fundamentos.md", "r", encoding="utf-8") as fundamentos:
    fundamentos = fundamentos.read()

with open("data/spring-boot/injecao-de-dependencias.md", "r", encoding="utf-8") as injecao_de_dependencias:
    injecao_de_dependencias = injecao_de_dependencias.read()

with open("docs/agente.md", "r", encoding="utf-8") as agente:
    agente = agente.read()

with open("prompts/system.md", "r", encoding="utf-8") as prompt_system:
    prompt_system = prompt_system.read()

resposta = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": prompt_system
        },
        {
            "role": "user",
            "content": input("Digite sua dúvida: ")
        }

    ]
)

print(resposta["message"]["content"])