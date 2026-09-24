# Injeção de Dependências

## 1. O que é uma dependência?

Uma dependência é um objeto ou componente que uma classe precisa para realizar seu trabalho.

Por exemplo, imagine um `ProdutoService` que precisa de um `ProdutoRepository` para buscar e salvar produtos.

```java
public class ProdutoService {

    private ProdutoRepository produtoRepository;

}
```

Nesse caso, o `ProdutoService` depende do `ProdutoRepository`.

### Quando utilizar

Sempre que uma classe precisar utilizar outra classe para realizar alguma responsabilidade.

### Exemplo prático

Em uma API de produtos:

```text
ProdutoController
        ↓
ProdutoService
        ↓
ProdutoRepository
```

O `ProdutoService` depende do `ProdutoRepository`, enquanto o `ProdutoController` depende do `ProdutoService`.

---

## 2. O que é Injeção de Dependências?

Injeção de Dependências (Dependency Injection — DI) é uma técnica na qual uma classe recebe suas dependências de fora, em vez de criá-las diretamente.

Sem injeção de dependência:

```java
public class ProdutoService {

    private ProdutoRepository produtoRepository =
            new ProdutoRepository();

}
```

A própria classe está criando sua dependência.

Com injeção de dependência:

```java
public class ProdutoService {

    private final ProdutoRepository produtoRepository;

    public ProdutoService(ProdutoRepository produtoRepository) {
        this.produtoRepository = produtoRepository;
    }

}
```

Agora o `ProdutoService` recebe o `ProdutoRepository`.

### Ideia principal

> A classe não deve ser responsável por criar suas dependências. Ela deve receber aquilo de que precisa.

---

## 3. Por que utilizar Injeção de Dependências?

A injeção de dependências ajuda a reduzir o acoplamento entre as classes.

Quando uma classe cria diretamente suas dependências, ela fica mais ligada a implementações específicas.

Com DI, a dependência pode ser fornecida externamente.

Isso facilita:

* manutenção;
* testes;
* substituição de implementações;
* reutilização;
* organização do código;
* baixo acoplamento.

---

## 4. Injeção por construtor

No Spring, uma das formas mais utilizadas de realizar a injeção de dependências é através do construtor.

```java
@Service
public class ProdutoService {

    private final ProdutoRepository produtoRepository;

    public ProdutoService(ProdutoRepository produtoRepository) {
        this.produtoRepository = produtoRepository;
    }
}
```

O `ProdutoService` declara que precisa de um `ProdutoRepository`.

O Spring identifica essa dependência e fornece um objeto gerenciado por ele.

### Por que utilizar `final`?

```java
private final ProdutoRepository produtoRepository;
```

O `final` indica que a referência deve ser definida uma vez, normalmente no construtor.

Isso ajuda a deixar claro que essa dependência é necessária para o funcionamento da classe.

### Observação

Quando existe apenas um construtor, o Spring consegue realizar a injeção automaticamente. Portanto, não é necessário utilizar `@Autowired` no construtor nesse caso.

---

## 5. O que é um Bean?

Bean é um objeto que é criado e gerenciado pelo Spring.

Por exemplo:

```java
@Service
public class ProdutoService {
}
```

O Spring identifica essa classe como um componente e cria uma instância dela para ser utilizada pela aplicação.

O mesmo acontece com componentes como:

```java
@Repository
public interface ProdutoRepository extends JpaRepository<Produto, Integer> {
}
```

```java
@Component
public class ProdutoMapper {
}
```

Esses componentes podem ser gerenciados pelo Spring e utilizados como dependências de outras classes.

---

## 6. O que é o Container do Spring?

O Spring possui um mecanismo responsável por criar, configurar e gerenciar os Beans da aplicação.

Esse mecanismo é chamado de **IoC Container**.

IoC significa **Inversion of Control** — Inversão de Controle.

Em vez de cada classe controlar a criação das suas dependências, o Spring assume essa responsabilidade.

Exemplo:

```text
Aplicação
    ↓
Spring Container
    ↓
Cria e gerencia os Beans
    ↓
Injeta as dependências necessárias
```

Por isso, quando temos:

```java
@Service
public class ProdutoService {

    private final ProdutoRepository produtoRepository;

    public ProdutoService(ProdutoRepository produtoRepository) {
        this.produtoRepository = produtoRepository;
    }
}
```

O Spring procura um `ProdutoRepository` disponível e o fornece ao `ProdutoService`.

---

## 7. Principais anotações relacionadas

### `@Component`

Indica que uma classe pode ser gerenciada pelo Spring.

```java
@Component
public class ProdutoMapper {
}
```

É uma anotação genérica para componentes.

---

### `@Service`

Indica que a classe representa uma camada de serviço, normalmente contendo regras de negócio.

```java
@Service
public class ProdutoService {
}
```

É uma especialização de `@Component`.

---

### `@Repository`

Normalmente utilizada em componentes responsáveis pelo acesso aos dados.

```java
@Repository
public interface ProdutoRepository {
}
```

Também é uma especialização de `@Component`.

No Spring Data, interfaces de repositório como `JpaRepository` são implementadas e gerenciadas pelo Spring.

---

### `@Controller`

Indica uma classe responsável por receber requisições relacionadas à camada web.

```java
@Controller
public class ProdutoController {
}
```

---

### `@RestController`

É utilizada principalmente na criação de APIs REST.

```java
@RestController
public class ProdutoController {
}
```

Ela combina o comportamento de `@Controller` com `@ResponseBody`.

---

## 8. Injeção de uma interface

A injeção de dependências fica ainda mais interessante quando trabalhamos com interfaces.

Imagine:

```java
public interface Pagamento {
    void pagar();
}
```

Podemos ter diferentes implementações:

```java
public class PagamentoPix implements Pagamento {

    @Override
    public void pagar() {
        // pagamento via PIX
    }
}
```

```java
public class PagamentoCartao implements Pagamento {

    @Override
    public void pagar() {
        // pagamento via cartão
    }
}
```

Uma classe pode depender da abstração:

```java
public class PedidoService {

    private final Pagamento pagamento;

    public PedidoService(Pagamento pagamento) {
        this.pagamento = pagamento;
    }
}
```

O `PedidoService` não precisa conhecer diretamente uma implementação específica.

Ele depende da interface `Pagamento`.

### Benefício

Isso reduz o acoplamento e facilita a substituição da implementação.

Por exemplo:

```text
PedidoService
      ↓
   Pagamento
      ↑
 ┌────┴─────┐
 PIX       Cartão
```

O serviço trabalha com a abstração, e não diretamente com uma implementação específica.

---

## 9. Injeção de Dependências e baixo acoplamento

A Injeção de Dependências está diretamente relacionada ao conceito de **baixo acoplamento**.

Sem DI:

```text
ProdutoService
      ↓
new ProdutoRepository()
```

O `ProdutoService` controla a criação da dependência.

Com DI:

```text
ProdutoService
      ↑
      |
Spring fornece
      |
ProdutoRepository
```

A responsabilidade de criação é transferida para o Spring.

Isso permite que as classes se concentrem em suas próprias responsabilidades.

---

## 10. Injeção de Dependências e alta coesão

DI também contribui para manter as responsabilidades bem separadas.

Por exemplo:

```text
Controller
   ↓
recebe requisição

Service
   ↓
executa regras de negócio

Repository
   ↓
acessa dados
```

Cada componente possui uma responsabilidade principal.

O Controller não precisa criar o Service.

O Service não precisa criar o Repository.

O Spring realiza a ligação entre esses componentes.

---

## 11. Exemplo prático em uma API

Imagine uma API de produtos.

### Repository

```java
@Repository
public interface ProdutoRepository
        extends JpaRepository<Produto, Integer> {
}
```

### Service

```java
@Service
public class ProdutoService {

    private final ProdutoRepository produtoRepository;

    public ProdutoService(ProdutoRepository produtoRepository) {
        this.produtoRepository = produtoRepository;
    }
}
```

### Controller

```java
@RestController
@RequestMapping("/produtos")
public class ProdutoController {

    private final ProdutoService produtoService;

    public ProdutoController(ProdutoService produtoService) {
        this.produtoService = produtoService;
    }
}
```

O fluxo fica:

```text
Cliente
   ↓
ProdutoController
   ↓
ProdutoService
   ↓
ProdutoRepository
   ↓
Banco de dados
```

Cada classe recebe aquilo de que precisa.

---

## 12. Erros comuns de iniciantes

### Criar dependências com `new` dentro do Service

Evite:

```java
ProdutoRepository repository = new ProdutoRepository();
```

Quando o objeto é um componente que deve ser gerenciado pelo Spring, o ideal é permitir que o Spring forneça essa dependência.

---

### Colocar toda a lógica no Controller

O Controller deve lidar principalmente com a comunicação HTTP.

Regras de negócio normalmente pertencem ao Service.

---

### Confundir DI com criação de objetos

A ideia principal da DI não é simplesmente "o Spring cria objetos".

O ponto principal é:

> Uma classe recebe de fora aquilo de que depende.

---

### Usar `@Autowired` sem entender o motivo

É importante primeiro entender a injeção por construtor.

Em uma classe com apenas um construtor, o Spring consegue realizar a injeção sem precisar colocar `@Autowired` nele.

---

## 13. Dúvidas comuns

### "Injeção de dependência é exclusiva do Spring?"

Não.

DI é um conceito de desenvolvimento de software.

O Spring fornece mecanismos para facilitar sua utilização.

---

### "O Spring cria qualquer objeto automaticamente?"

Não.

Para que uma classe seja gerenciada pelo Spring, ela normalmente precisa ser identificada como um componente, por exemplo através de `@Component`, `@Service`, `@Repository`, `@Controller` ou `@RestController`, ou ser registrada de outra forma.

---

### "Por que não usar `new`?"

O problema não é o `new` existir.

Ele continua sendo utilizado normalmente em Java.

A questão é evitar que classes gerenciadas pelo Spring tenham que controlar manualmente a criação de suas dependências.

---

### "DI elimina o acoplamento?"

Não.

A aplicação continua tendo dependências.

O objetivo é reduzir o acoplamento desnecessário e permitir que as dependências sejam substituídas com mais facilidade.

---

## 14. Relação com outros conceitos

A Injeção de Dependências está relacionada principalmente a:

```text
POO
 ↓
Classes e objetos
 ↓
Dependências
 ↓
Injeção de Dependências
 ↓
Inversão de Controle
 ↓
Baixo acoplamento
 ↓
Arquitetura organizada
```

No Spring Boot, esses conceitos aparecem juntos constantemente.

Por exemplo:

```text
@RestController
      ↓
   Service
      ↓
 Repository
```

Cada componente possui uma responsabilidade e recebe suas dependências do Spring.

---

## 15. Resumo

**Dependência:** objeto que uma classe precisa para realizar seu trabalho.

**Injeção de Dependências:** técnica em que uma classe recebe suas dependências de fora, em vez de criá-las diretamente.

**Bean:** objeto gerenciado pelo Spring.

**IoC:** princípio no qual o controle sobre a criação e gerenciamento dos objetos é transferido para o framework.

**Constructor Injection:** forma de injetar uma dependência através do construtor.

**`@Component`:** identifica um componente gerenciado pelo Spring.

**`@Service`:** representa normalmente a camada de regras de negócio.

**`@Repository`:** representa normalmente a camada de acesso a dados.

**Benefício principal:** reduzir acoplamento e organizar melhor as responsabilidades da aplicação.
