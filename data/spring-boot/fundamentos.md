# Fundamentos do Spring Boot

## 1. O que é Spring Boot?

### Conceito

Spring Boot é uma ferramenta baseada no ecossistema Spring que facilita a criação e configuração de aplicações Java.

Ele fornece configurações e recursos que reduzem a quantidade de configuração necessária para iniciar uma aplicação Spring, permitindo que o desenvolvedor se concentre mais na implementação das funcionalidades da aplicação.

### Para que serve?

Spring Boot é utilizado para desenvolver aplicações Java, incluindo APIs REST, aplicações web e sistemas corporativos.

### Por que utilizar Spring Boot?

Entre os principais benefícios estão:

* configuração simplificada;
* integração com diversas tecnologias;
* suporte à injeção de dependências;
* facilidade para criar APIs REST;
* organização de aplicações em componentes;
* possibilidade de utilizar diferentes projetos do ecossistema Spring.

---

## 2. Estrutura básica de uma aplicação Spring Boot

### Conceito

Uma aplicação Spring Boot normalmente possui uma classe principal responsável por iniciar a aplicação.

Também é comum organizar o código em diferentes componentes de acordo com suas responsabilidades.

Uma estrutura comum para uma API pode ser:

```text id="7v6nq0"
src/
└── main/
    └── java/
        └── com.exemplo.projeto/
            ├── ProjetoApplication.java
            ├── controller/
            ├── service/
            ├── repository/
            └── model/
```

Essa organização pode variar de acordo com o projeto.

### Sintaxe

A classe principal de uma aplicação Spring Boot normalmente utiliza `@SpringBootApplication`:

```java id="3l0m8c"
@SpringBootApplication
public class ProjetoApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProjetoApplication.class, args);
    }
}
```

### Quando utilizar?

A classe principal é utilizada como ponto de inicialização da aplicação Spring Boot.

### Exemplo prático

Ao executar:

```java id="q9t3zv"
SpringApplication.run(ProjetoApplication.class, args);
```

o Spring Boot inicializa o contexto da aplicação e os componentes necessários para que a aplicação funcione.

### Erros comuns

* Não entender que a classe principal é responsável por iniciar a aplicação.
* Colocar a classe principal em um pacote que dificulte a descoberta dos componentes pelo Spring.
* Confundir Spring Framework com Spring Boot.

### Relação com outros conceitos

A inicialização da aplicação está relacionada ao contexto do Spring, ao mecanismo de componentes e à injeção de dependências.

---

# 3. `@SpringBootApplication`

### Conceito

`@SpringBootApplication` é uma anotação utilizada na classe principal de uma aplicação Spring Boot.

Ela combina funcionalidades importantes para a configuração e inicialização da aplicação.

De forma simplificada, ela reúne funcionalidades relacionadas a:

* configuração da aplicação;
* configuração automática;
* descoberta de componentes.

### Sintaxe

```java id="l4g0tb"
@SpringBootApplication
public class ProjetoApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProjetoApplication.class, args);
    }
}
```

### Quando utilizar?

Normalmente é utilizada na classe principal de uma aplicação Spring Boot para indicar ao Spring que aquela classe participa da configuração e inicialização da aplicação.

### Exemplo prático

```java id="1h7w5x"
package com.exemplo.projeto;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ProjetoApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProjetoApplication.class, args);
    }
}
```

Ao iniciar essa classe, a aplicação Spring Boot é inicializada.

### Erros comuns

* Esquecer a anotação na classe principal.
* Não compreender que a anotação reúne diferentes funcionalidades do Spring.
* Colocar a classe principal em uma localização que dificulte o component scanning.

### Relação com outros conceitos

`@SpringBootApplication` está relacionada à configuração automática e à descoberta dos componentes da aplicação.

---

# 4. Componentes do Spring

### Conceito

O Spring permite registrar classes como componentes gerenciados pelo framework.

Esses componentes podem ser identificados por diferentes anotações de acordo com sua responsabilidade.

Algumas das principais são:

```text id="yq1r0s"
@Component
@Service
@Repository
@Controller
@RestController
```

O Spring pode criar e gerenciar objetos dessas classes dentro do seu contexto.

### Sintaxe

Exemplo:

```java id="f8d9al"
@Service
public class ProdutoService {

}
```

### Quando utilizar?

As anotações devem ser utilizadas de acordo com a responsabilidade da classe.

Por exemplo:

* `@Service` → lógica de negócio;
* `@Repository` → acesso a dados;
* `@Controller` → controle de requisições web;
* `@RestController` → controle de requisições para APIs REST;
* `@Component` → componente genérico gerenciado pelo Spring.

### Exemplo prático

Uma API pode possuir:

```text id="o2q3sk"
ProdutoController
        ↓
ProdutoService
        ↓
ProdutoRepository
```

Cada componente possui uma responsabilidade diferente.

### Erros comuns

* Colocar toda a lógica da aplicação no controller.
* Utilizar `@Component` sem entender a responsabilidade da classe.
* Confundir `@Service` com `@Repository`.
* Acreditar que as anotações são apenas marcadores sem função no funcionamento do Spring.

### Relação com outros conceitos

Os componentes estão diretamente relacionados à **injeção de dependência**, que será abordada em outro arquivo da base.

---

# 5. Configuração automática

### Conceito

Uma das características do Spring Boot é a configuração automática.

Com base nas dependências presentes no projeto e nas configurações disponíveis, o Spring Boot pode realizar diversas configurações automaticamente.

Isso reduz a quantidade de configuração manual necessária para iniciar uma aplicação.

### Sintaxe

A configuração automática está relacionada à utilização de:

```java id="9bq8vl"
@SpringBootApplication
```

e às dependências adicionadas ao projeto.

### Quando utilizar?

A configuração automática é utilizada durante a inicialização da aplicação Spring Boot.

O desenvolvedor geralmente precisa apenas configurar os recursos específicos do projeto quando necessário.

### Exemplo prático

Ao adicionar uma dependência para desenvolvimento de uma API REST, o Spring Boot pode fornecer automaticamente diversas configurações necessárias para que a aplicação web funcione.

### Erros comuns

* Pensar que o Spring Boot configura absolutamente tudo.
* Não entender que configurações específicas ainda podem ser necessárias.
* Não saber identificar quando uma configuração automática está interferindo no comportamento esperado.

### Relação com outros conceitos

A configuração automática faz parte dos recursos que diferenciam a experiência de desenvolvimento com Spring Boot e está relacionada ao conceito de `@SpringBootApplication`.

---

# 6. Organização por responsabilidades

### Conceito

Uma aplicação Spring Boot pode separar suas responsabilidades em diferentes componentes.

Uma organização comum em uma API é:

```text id="xjv1l2"
Controller
    ↓
Service
    ↓
Repository
```

O objetivo dessa separação é evitar que uma única classe concentre todas as responsabilidades da aplicação.

### Quando utilizar?

Essa organização é utilizada para estruturar aplicações e separar responsabilidades.

### Exemplo prático

Em uma API de produtos:

```text id="l2v8k3"
ProdutoController
→ recebe requisições HTTP

ProdutoService
→ executa regras de negócio

ProdutoRepository
→ realiza operações relacionadas aos dados
```

### Erros comuns

* Colocar regras de negócio diretamente no controller.
* Fazer o repository executar regras que pertencem ao service.
* Criar classes sem uma responsabilidade clara.

### Relação com outros conceitos

A separação de responsabilidades está relacionada à alta coesão e ao baixo acoplamento.

---

# 7. Situação prática

Imagine uma API para gerenciamento de produtos.

O projeto pode possuir:

```text id="0b2s9f"
ProdutoController
ProdutoService
ProdutoRepository
```

Quando o cliente envia uma requisição para cadastrar um produto:

```text id="xj7d5m"
Cliente
   ↓
HTTP Request
   ↓
ProdutoController
   ↓
ProdutoService
   ↓
ProdutoRepository
   ↓
Banco de dados
```

Cada componente participa de uma parte do processo.

O controller não precisa conhecer todos os detalhes de persistência, e o repository não precisa conhecer as regras de negócio da aplicação.

---

# 8. Dúvidas e erros comuns de iniciantes

### "Spring Boot e Spring são a mesma coisa?"

Não exatamente.

Spring é um ecossistema/framework para desenvolvimento Java. Spring Boot é uma ferramenta do ecossistema Spring que facilita a configuração e inicialização de aplicações.

### "O Spring Boot substitui o Java?"

Não.

Spring Boot é utilizado para desenvolver aplicações utilizando Java e os recursos do ecossistema Spring.

### "Toda classe precisa de uma anotação do Spring?"

Não.

Existem classes que não precisam ser componentes gerenciados pelo Spring.

### "Por que separar Controller, Service e Repository?"

Para organizar responsabilidades e evitar que uma única classe concentre diferentes funções da aplicação.

### "O Spring cria todos os objetos automaticamente?"

O Spring gerencia objetos que fazem parte do seu contexto, especialmente os componentes registrados de acordo com suas configurações e anotações.

---

# 9. Relação com outros conceitos

Os fundamentos do Spring Boot servem como base para compreender outros conceitos da aplicação.

```text id="q6xw8e"
Spring Boot
    │
    ├── @SpringBootApplication
    │
    ├── Componentes
    │     ├── @Controller
    │     ├── @Service
    │     └── @Repository
    │
    ├── Injeção de Dependência
    │
    └── APIs REST
```

A compreensão desses fundamentos facilita o estudo de injeção de dependência e desenvolvimento de APIs REST.

---

# 10. Resumo

Spring Boot facilita o desenvolvimento de aplicações Java utilizando o ecossistema Spring.

Uma aplicação Spring Boot possui uma classe principal que normalmente utiliza `@SpringBootApplication` para iniciar a aplicação.

O Spring permite organizar a aplicação em componentes com responsabilidades diferentes, como:

* `@Controller`;
* `@RestController`;
* `@Service`;
* `@Repository`;
* `@Component`.

A separação dessas responsabilidades ajuda a construir aplicações mais organizadas e está relacionada aos conceitos de alta coesão e baixo acoplamento.

Os fundamentos de Spring Boot servem como base para compreender conceitos mais específicos, como **injeção de dependência e APIs REST**.
