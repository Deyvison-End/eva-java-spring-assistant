# 🤖 Eva — Java & Spring Mentor

Assistente virtual com Inteligência Artificial desenvolvido para auxiliar programadores iniciantes no aprendizado de **Java e Spring Boot**.

## 📌 Sobre o Projeto

A **Eva** é um assistente virtual educacional criado para ajudar pessoas que estão começando a aprender Java e Spring Boot.

O objetivo não é apenas responder dúvidas, mas ajudar o usuário a **compreender conceitos, entender sua sintaxe e perceber como aplicá-los na prática**.

Além das explicações, a Eva pode propor perguntas e exercícios para ajudar na consolidação do aprendizado.

## 🎯 Problema

Pessoas que estão começando a aprender Java e Spring Boot podem ter dificuldade para:

* compreender determinados conceitos;
* entender a sintaxe;
* saber quando utilizar determinado recurso;
* relacionar conceitos teóricos com situações práticas;
* verificar se realmente compreenderam determinado assunto.

## 💡 Solução

A Eva busca solucionar esse problema oferecendo uma experiência de aprendizado baseada em:

* explicação de conceitos;
* apresentação de sintaxe;
* exemplos de aplicação prática;
* perguntas para estimular o raciocínio;
* exercícios para consolidação do conhecimento;
* feedback sobre as respostas do usuário;
* orientação quando uma informação não estiver disponível em sua base de conhecimento.

A proposta é fazer com que o usuário **participe do processo de aprendizagem**, em vez de apenas receber respostas prontas.

## 👤 Público-Alvo

Programadores iniciantes que estão aprendendo:

* Java;
* Spring Boot;
* conceitos fundamentais de desenvolvimento backend.

## 🧠 Como a Eva Ensina

A interação segue uma abordagem baseada em aprendizado ativo.

```text
Usuário faz uma pergunta
        ↓
Eva explica o conceito
        ↓
Relaciona com uma aplicação prática
        ↓
Eva pergunta se o usuário quer praticar
        ↓
       Sim
        ↓
Gera pergunta ou exercício
        ↓
Usuário responde
        ↓
Eva avalia a resposta
        ↓
Feedback e nova tentativa
```

Quando o usuário apresentar uma resposta incorreta ou parcialmente correta, a Eva procura compreender seu raciocínio e fornece pistas ou pequenas explicações antes de apresentar diretamente a solução.

Caso o usuário continue com dificuldade, a Eva pode perguntar se ele deseja uma explicação mais detalhada.

## 🛡️ Controle de Respostas

A Eva possui como princípio evitar respostas inventadas.

Quando uma informação não estiver disponível em sua base de conhecimento, o agente deve:

* informar que não encontrou a informação na base;
* evitar apresentar uma informação como se fosse validada pela base;
* indicar conceitos relacionados que podem ajudar no aprendizado;
* sugerir caminhos para estudar o assunto;
* quando oferecer conhecimento complementar, deixar claro que se trata de uma explicação complementar.

## 📚 Base de Conhecimento

A base de conhecimento será construída com conteúdos relacionados a:

### Java

* [ ] Conceitos fundamentais
* [ ] Classes e objetos
* [ ] Interfaces
* [ ] Herança
* [ ] Collections
* [ ] Exceptions

### Spring Boot

* [ ] Spring Boot
* [ ] Controllers
* [ ] Services
* [ ] Dependency Injection
* [ ] DTOs
* [ ] APIs REST

> A definição final dos conteúdos será realizada durante a construção da base de conhecimento.

## 🚀 Funcionalidades

* [ ] Responder dúvidas sobre Java
* [ ] Responder dúvidas sobre Spring Boot
* [ ] Explicar conceitos
* [ ] Explicar sintaxe
* [ ] Mostrar aplicações práticas
* [ ] Perguntar se o usuário deseja praticar
* [ ] Gerar perguntas e exercícios
* [ ] Avaliar respostas do usuário
* [ ] Fornecer pistas quando o usuário errar
* [ ] Permitir novas tentativas
* [ ] Indicar limitações quando não houver informação suficiente

## 🏗️ Estrutura do Projeto

```text
eva-java-spring-mentor/
│
├── README.md
│
├── data/
│   └── Base de conhecimento
│
├── docs/
│   └── agente.md
│
└── src/
    └── Aplicação
```

## 🛠️ Tecnologias

As tecnologias utilizadas no projeto serão definidas durante a etapa de desenvolvimento.

* [ ] Linguagem / Framework
* [ ] Modelo de IA / API
* [ ] Int
