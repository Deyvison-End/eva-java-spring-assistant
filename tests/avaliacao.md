# Avaliação da Eva

## Objetivo

Avaliar o desempenho da Eva como assistente virtual de aprendizagem para desenvolvedores iniciantes em Java e Spring Boot.

A avaliação considera três aspectos principais:

* **Correção técnica**
* **Ensino para iniciantes**
* **Fidelidade à base de conhecimento e ao escopo**

---

## Critérios de avaliação

### 1. Correção técnica

Avalia se o conceito apresentado pela Eva está correto e se a explicação faz sentido dentro do contexto da pergunta.

### 2. Ensino para iniciantes

Avalia se a explicação é clara, compreensível e adequada para uma pessoa que está iniciando em Java e Spring Boot.

### 3. Fidelidade à base de conhecimento e ao escopo

Avalia se a Eva utiliza corretamente a base de conhecimento, permanece dentro do escopo definido e evita inventar informações (alucinações).

---

## Escala de avaliação

Todos os critérios utilizam uma escala de **0 a 5**:

| Nota | Descrição                                      |
| ---- | ---------------------------------------------- |
| 0    | Não atende ao critério                         |
| 1    | Atende muito pouco                             |
| 2    | Atende parcialmente, com problemas importantes |
| 3    | Atende de forma razoável                       |
| 4    | Atende bem, com pequenos problemas             |
| 5    | Atende completamente ao critério               |

---

## Teste geral

O primeiro teste será composto por cinco perguntas, buscando avaliar diferentes conhecimentos e também o comportamento da Eva diante de uma pergunta fora do seu escopo.

| # | Pergunta                             | Correção técnica | Ensino para iniciantes | Fidelidade à base/escopo |
| - | ------------------------------------ | ---------------: | ---------------------: | -----------------------: |
| 1 | O que é e como criar método em Java? |                — |                      — |                        — |
| 2 | O que é uma classe?                  |                — |                      — |                        — |
| 3 | O que é uma classe coesa?            |                — |                      — |                        — |
| 4 | O que é `@Service` em Spring Boot?   |                — |                      — |                        — |
| 5 | Qual a previsão do tempo hoje?       |                — |                      — |                        — |

---

## Comportamento esperado

### Pergunta 1 — Métodos em Java

Uma resposta com nota máxima deve apresentar:

* o conceito de método;
* a sintaxe de um método;
* a explicação de cada parte da sintaxe;
* para que o método serve;
* um exemplo;
* uma explicação clara para um iniciante.

### Pergunta 2 — Classes

Uma resposta com nota máxima deve:

* explicar o conceito de classe;
* explicar seu significado em Java;
* apresentar um exemplo;
* explicar o exemplo de forma clara.

### Pergunta 3 — Classe coesa

Uma resposta com nota máxima deve:

* explicar o conceito de coesão;
* mostrar o que caracteriza uma classe coesa;
* mostrar o que caracteriza uma classe não coesa;
* deixar clara a diferença entre as duas;
* utilizar exemplos compreensíveis.

### Pergunta 4 — `@Service`

Uma resposta com nota máxima deve:

* explicar o conceito de `@Service`;
* apresentar sua sintaxe;
* explicar onde é aplicado;
* explicar para que serve;
* apresentar um exemplo;
* explicar o exemplo de forma clara.

### Pergunta 5 — Previsão do tempo

Como a pergunta está fora do escopo da Eva, uma resposta com nota máxima deve:

* reconhecer que a pergunta está fora do escopo;
* informar que não pode respondê-la;
* não inventar uma previsão do tempo.

---

## Resultado

Os resultados serão preenchidos após a execução dos testes.

| # | Correção técnica | Ensino para iniciantes | Fidelidade à base/escopo | Média |
| - | ---------------: | ---------------------: | -----------------------: | ----: |
| 1 |                — |                      — |                        — |     — |
| 2 |                — |                      — |                        — |     — |
| 3 |                — |                      — |                        — |     — |
| 4 |                — |                      — |                        — |     — |
| 5 |                — |                      — |                        — |     — |

### Observações

As observações serão utilizadas para identificar pontos fortes, limitações e possíveis melhorias no comportamento da Eva.

---

## Próximas avaliações

Após o teste geral, serão realizados testes específicos para analisar individualmente aspectos como:

* correção técnica;
* capacidade de ensino;
* fidelidade à base de conhecimento;
* comportamento fora do escopo;
* ocorrência de alucinações.

## Testes específicos

Após o teste geral, serão realizados testes específicos para avaliar individualmente cada aspecto do comportamento da Eva.

Cada critério será avaliado com **duas perguntas**, utilizando a mesma escala de **0 a 5** definida anteriormente.

---

### 1. Correção técnica

Objetivo: verificar se a Eva apresenta conceitos tecnicamente corretos e consegue explicar corretamente o conteúdo apresentado.

| #   | Pergunta                                                   | Nota |
| --- | ---------------------------------------------------------- | ---: |
| 1.1 | O que é encapsulamento em Java e por que ele é utilizado?  |    — |
| 1.2 | Qual a diferença entre uma classe e uma interface em Java? |    — |

**O que observar:**

* Se o conceito apresentado está tecnicamente correto;
* Se não existem afirmações contraditórias ou incorretas;
* Se os exemplos utilizados estão de acordo com o conceito;
* Se a resposta realmente responde à pergunta.

---

### 2. Ensino para iniciantes

Objetivo: verificar se a Eva consegue explicar um mesmo conteúdo de maneira adequada para diferentes níveis de conhecimento.

| #   | Pergunta                                                                                                               | Nível esperado       | Nota |
| --- | ---------------------------------------------------------------------------------------------------------------------- | -------------------- | ---: |
| 2.1 | Explique o que é herança em Java como se eu nunca tivesse programado antes.                                            | Iniciante            |    — |
| 2.2 | Já entendo o básico de orientação a objetos. Explique como a herança funciona em Java e quando faz sentido utilizá-la. | Básico/intermediário |    — |

**O que observar:**

* Se a linguagem utilizada é adequada ao nível indicado;
* Se a Eva evita excesso de termos técnicos para iniciantes;
* Se consegue aprofundar a explicação quando o usuário possui mais conhecimento;
* Se a explicação evolui de acordo com o contexto apresentado.

---

### 3. Fidelidade à base de conhecimento

Objetivo: verificar se a Eva utiliza corretamente os conhecimentos disponíveis na base e mantém suas respostas dentro do conteúdo definido para o projeto.

| #   | Pergunta                                                  | Nota |
| --- | --------------------------------------------------------- | ---: |
| 3.1 | O que é injeção de dependências no Spring Boot?           |    — |
| 3.2 | O que é coesão e como ela se relaciona com o acoplamento? |    — |

**O que observar:**

* Se a resposta está de acordo com os conteúdos presentes na base;
* Se a Eva não contradiz as informações da base;
* Se utiliza os conceitos apresentados nos arquivos de conhecimento;
* Se não adiciona informações desnecessárias que possam fugir do conteúdo disponível.

---

### 4. Alucinação

Objetivo: verificar se a Eva evita inventar informações quando recebe uma pergunta sobre um assunto que não está presente em sua base de conhecimento.

| #   | Pergunta                                                        | Nota |
| --- | --------------------------------------------------------------- | ---: |
| 4.1 | Como configurar um banco de dados MongoDB no Spring Boot?       |    — |
| 4.2 | Como implementar autenticação OAuth2 com Google no Spring Boot? |    — |

**O que observar:**

* Se a Eva reconhece quando não possui conhecimento suficiente na base;
* Se evita apresentar informações como se fossem conhecidas quando não estão disponíveis;
* Se deixa clara sua limitação;
* Se não inventa conceitos, configurações ou informações.

---

### 5. Escopo

Objetivo: verificar se a Eva reconhece perguntas que não possuem relação com Java ou Spring Boot e evita responder como se fossem parte de seu domínio.

| #   | Pergunta                         | Nota |
| --- | -------------------------------- | ---: |
| 5.1 | Qual é a capital da França?      |    — |
| 5.2 | Como fazer um bolo de chocolate? |    — |

**O que observar:**

* Se a Eva reconhece que a pergunta está fora de seu escopo;
* Se evita responder diretamente a assuntos que não fazem parte de Java e Spring Boot;
* Se mantém seu papel de assistente de aprendizagem;
* Se não tenta relacionar artificialmente a pergunta com programação apenas para fornecer uma resposta.

