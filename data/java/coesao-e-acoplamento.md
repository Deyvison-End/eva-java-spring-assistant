# Coesão e Acoplamento

## 1. O que é Coesão?

### Conceito

Coesão representa o quanto as responsabilidades de uma classe, módulo ou componente estão relacionadas entre si.

Uma classe possui **alta coesão** quando suas responsabilidades estão relacionadas e fazem parte de um mesmo propósito.

Por exemplo, uma classe `Produto` pode ser responsável por informações e comportamentos diretamente relacionados a um produto.

```java
public class Produto {

    private String nome;
    private double preco;

    public void aplicarDesconto(double percentual) {
        this.preco -= this.preco * percentual;
    }
}
```

Nesse exemplo, os atributos e o comportamento estão relacionados ao conceito de produto.

### Para que serve?

A coesão ajuda a organizar responsabilidades dentro do sistema, tornando as classes mais fáceis de entender, manter e modificar.

### Por que buscar alta coesão?

Classes com alta coesão tendem a possuir responsabilidades mais bem definidas.

Isso facilita:

* compreensão do código;
* manutenção;
* testes;
* reutilização;
* identificação de mudanças necessárias.

---

## 2. Alta Coesão

### Conceito

Alta coesão significa que uma classe ou componente possui responsabilidades fortemente relacionadas entre si.

Por exemplo:

```java
public class Pedido {

    private BigDecimal valorTotal;

    public void calcularValorTotal() {
        // cálculo relacionado ao pedido
    }
}
```

A responsabilidade da classe está relacionada ao conceito de `Pedido`.

Um exemplo de baixa coesão seria uma classe que mistura responsabilidades completamente diferentes:

```java
public class Pedido {

    public void calcularValorTotal() {
        // ...
    }

    public void enviarEmail() {
        // ...
    }

    public void gerarRelatorioPDF() {
        // ...
    }

    public void conectarBancoDeDados() {
        // ...
    }
}
```

Nesse caso, a classe está assumindo responsabilidades relacionadas a pedido, email, relatório e banco de dados.

### Quando buscar alta coesão?

Ao projetar classes e componentes, procure manter juntas responsabilidades que pertencem ao mesmo contexto.

Uma pergunta útil é:

> "Essa responsabilidade realmente pertence a esta classe?"

### Exemplo prático

Em uma aplicação de vendas, podemos separar responsabilidades:

```text
PedidoService
    → regras relacionadas ao pedido

EmailService
    → envio de emails

RelatorioService
    → geração de relatórios
```

Cada componente possui uma responsabilidade mais específica.

### Erros comuns

* Colocar várias responsabilidades diferentes em uma única classe.
* Criar uma classe "faz tudo".
* Confundir reutilização de código com concentração de responsabilidades.
* Criar classes grandes demais.

### Relação com outros conceitos

Alta coesão está relacionada ao princípio de responsabilidade bem definida e pode contribuir para um código mais organizado e fácil de manter.

---

# 3. O que é Acoplamento?

### Conceito

Acoplamento representa o **grau de dependência entre diferentes classes ou componentes** de um sistema.

Quando uma classe depende fortemente de outra classe específica, existe um acoplamento maior entre elas.

Quando as dependências são reduzidas e bem controladas, temos menor acoplamento.

### Para que serve?

Compreender o acoplamento ajuda a avaliar o quanto uma alteração em uma parte do sistema pode afetar outras partes.

### Por que buscar baixo acoplamento?

O baixo acoplamento pode facilitar:

* manutenção;
* testes;
* substituição de implementações;
* evolução do sistema;
* reutilização de componentes.

---

## 4. Baixo Acoplamento

### Conceito

Baixo acoplamento significa reduzir dependências desnecessárias entre componentes.

Considere:

```java
public class PedidoService {

    private PagamentoPix pagamento = new PagamentoPix();

}
```

Nesse exemplo, `PedidoService` está diretamente ligado à implementação `PagamentoPix`.

Se quisermos utilizar cartão, boleto ou outra forma de pagamento, será necessário alterar `PedidoService`.

Uma alternativa é depender de uma abstração:

```java
public class PedidoService {

    private Pagamento pagamento;

    public PedidoService(Pagamento pagamento) {
        this.pagamento = pagamento;
    }
}
```

Nesse caso, `PedidoService` depende da abstração `Pagamento`, e diferentes implementações podem ser utilizadas.

### Quando utilizar?

Buscar baixo acoplamento é importante quando diferentes partes do sistema possuem responsabilidades independentes e podem precisar ser alteradas ou substituídas.

### Exemplo prático

Podemos definir uma interface:

```java
public interface Pagamento {

    void pagar();
}
```

E diferentes implementações:

```java
public class PagamentoPix implements Pagamento {

    @Override
    public void pagar() {
        System.out.println("Pagamento via PIX");
    }
}
```

```java
public class PagamentoCartao implements Pagamento {

    @Override
    public void pagar() {
        System.out.println("Pagamento via cartão");
    }
}
```

O código que utiliza `Pagamento` pode trabalhar com a abstração em vez de depender diretamente de uma implementação específica.

### Erros comuns

* Criar dependências diretas desnecessárias.
* Fazer uma classe conhecer detalhes internos de muitas outras classes.
* Acreditar que baixo acoplamento significa não possuir nenhuma dependência.
* Criar abstrações sem necessidade apenas para tentar reduzir acoplamento.

### Relação com outros conceitos

Baixo acoplamento está relacionado a:

* interfaces;
* abstração;
* injeção de dependência;
* separação de responsabilidades.

---

# 5. Relação entre Coesão e Acoplamento

Coesão e acoplamento são conceitos diferentes, mas estão relacionados à organização do sistema.

**Coesão** observa principalmente o que existe **dentro de um componente**.

**Acoplamento** observa principalmente a relação **entre diferentes componentes**.

Podemos pensar da seguinte forma:

```text
COESÃO
Dentro da classe
       ↓
As responsabilidades estão relacionadas?

ACOPLAMENTO
Entre classes
       ↓
Quanto uma classe depende de outra?
```

Um código bem organizado geralmente busca:

```text
Alta coesão
      +
Baixo acoplamento
```

Isso significa ter componentes com responsabilidades relacionadas e, ao mesmo tempo, evitar dependências desnecessárias ou excessivamente rígidas entre eles.

---

# 6. Situação prática

Imagine uma aplicação de vendas.

Uma implementação problemática poderia concentrar várias responsabilidades:

```java
public class Sistema {

    public void cadastrarCliente() {
        // ...
    }

    public void cadastrarProduto() {
        // ...
    }

    public void processarPedido() {
        // ...
    }

    public void enviarEmail() {
        // ...
    }

    public void gerarRelatorio() {
        // ...
    }
}
```

Essa classe possui muitas responsabilidades diferentes, o que pode dificultar sua manutenção.

Uma organização mais coesa poderia separar as responsabilidades:

```text
ClienteService
    → operações relacionadas a clientes

ProdutoService
    → operações relacionadas a produtos

PedidoService
    → operações relacionadas a pedidos

EmailService
    → envio de emails

RelatorioService
    → relatórios
```

Além disso, essas classes podem utilizar interfaces e injeção de dependência para reduzir dependências diretas entre implementações.

---

# 7. Dúvidas e erros comuns de iniciantes

### "Alta coesão significa uma classe ter apenas um método?"

Não.

Uma classe pode possuir vários métodos, desde que eles estejam relacionados à responsabilidade da classe.

### "Baixo acoplamento significa que as classes não podem depender umas das outras?"

Não.

Sistemas reais possuem dependências. O objetivo é evitar dependências desnecessárias ou excessivamente rígidas.

### "Alta coesão e baixo acoplamento são a mesma coisa?"

Não.

A coesão está relacionada principalmente às responsabilidades dentro de um componente.

O acoplamento está relacionado às dependências entre componentes.

### "Sempre devo criar uma interface para diminuir acoplamento?"

Não.

Interfaces podem ajudar a reduzir acoplamento em determinadas situações, mas criar abstrações sem necessidade também pode aumentar a complexidade do sistema.

---

# 8. Relação com Java e Spring Boot

Esses conceitos aparecem frequentemente em aplicações Java e Spring Boot.

Por exemplo, uma aplicação pode separar responsabilidades entre:

```text
Controller
    ↓
Service
    ↓
Repository
```

Cada camada possui uma responsabilidade diferente.

A injeção de dependência do Spring também pode ajudar a reduzir o acoplamento entre classes, permitindo que uma classe receba suas dependências em vez de criá-las diretamente.

Interfaces também podem ser utilizadas para permitir que uma classe dependa de uma abstração em vez de uma implementação específica.

---

# 9. Resumo

**Coesão** representa o quanto as responsabilidades de um componente estão relacionadas.

**Alta coesão** significa manter responsabilidades relacionadas juntas e evitar que uma classe acumule funções que pertencem a contextos diferentes.

**Acoplamento** representa o grau de dependência entre componentes.

**Baixo acoplamento** significa reduzir dependências desnecessárias ou excessivamente rígidas entre componentes.

Um objetivo comum no desenvolvimento de software é buscar:

> **Alta coesão e baixo acoplamento.**

Esses conceitos ajudam a construir sistemas mais organizados, compreensíveis e mais fáceis de modificar.
