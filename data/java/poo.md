# Programação Orientada a Objetos (POO)

## 1. O que é POO?

### Conceito

Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código a partir de **objetos**, que representam elementos de um sistema. Esses objetos possuem **características**, representadas por atributos, e **comportamentos**, representados por métodos.

A POO permite organizar o código de forma que diferentes responsabilidades sejam distribuídas entre classes e objetos.

### Para que serve?

A POO serve para organizar e estruturar sistemas, permitindo representar elementos do problema dentro do código e separar responsabilidades entre diferentes classes.

### Por que utilizar POO?

A utilização de POO pode facilitar a organização, manutenção e reutilização do código. Ela também fornece mecanismos como encapsulamento, herança e interfaces para estruturar melhor as relações e responsabilidades entre diferentes partes de um sistema.

---

## 2. Classes e Objetos

### Conceito

Uma **classe** é uma estrutura que define características e comportamentos que os objetos daquele tipo podem possuir.

Um **objeto** é uma instância de uma classe. Ele representa uma ocorrência concreta daquela estrutura.

Por exemplo, em um sistema de loja, `Produto` pode ser uma classe. Um produto específico, como um celular, pode ser representado por um objeto dessa classe.

A classe funciona como uma definição, enquanto o objeto representa uma instância dessa definição.

### Sintaxe

Uma classe pode ser declarada utilizando a palavra-chave `class`:

```java
public class Produto {

}
```

Um objeto pode ser criado utilizando `new`:

```java
Produto produto = new Produto();
```

### Quando utilizar?

Classes devem ser utilizadas para representar estruturas e responsabilidades do sistema.

Objetos são utilizados quando precisamos trabalhar com uma instância concreta de uma classe durante a execução do programa.

### Exemplo prático

```java
public class Produto {
    String nome;
    double preco;
}
```

Criando um objeto:

```java
Produto produto = new Produto();

produto.nome = "Notebook";
produto.preco = 3500.00;
```

Nesse exemplo, `Produto` é a classe e `produto` é um objeto criado a partir dela.

### Erros comuns

* Confundir classe com objeto.
* Pensar que uma classe e um objeto são exatamente a mesma coisa.
* Tentar utilizar um objeto sem instanciá-lo quando a situação exige uma instância.
* Criar classes sem uma responsabilidade clara.

### Relação com outros conceitos

Classes podem possuir atributos e métodos. Objetos utilizam essas características e comportamentos definidos pela classe.

---

## 3. Atributos

### Conceito

Atributos representam as **características ou dados** de um objeto.

Por exemplo, um objeto `Produto` pode possuir os atributos `nome`, `preco` e `quantidadeEstoque`.

### Sintaxe

Um atributo é declarado dentro da classe:

```java
public class Produto {

    private String nome;
    private double preco;
    private int quantidadeEstoque;

}
```

### Quando utilizar?

Atributos devem ser utilizados quando uma classe precisa armazenar informações relacionadas ao estado de seus objetos.

### Exemplo prático

```java
public class Cliente {

    private String nome;
    private String email;

}
```

Um objeto `Cliente` pode possuir um nome e um email diferentes de outro objeto da mesma classe.

### Erros comuns

* Criar atributos que não possuem relação com a responsabilidade da classe.
* Expor diretamente atributos que deveriam estar protegidos pelo encapsulamento.
* Confundir atributo com método.

### Relação com outros conceitos

Atributos representam características dos objetos. Métodos representam comportamentos. O encapsulamento pode ser utilizado para controlar o acesso aos atributos.

---

## 4. Métodos

### Conceito

Métodos representam **comportamentos ou ações** que uma classe pode executar.

Enquanto os atributos representam dados ou características, os métodos representam ações relacionadas ao objeto.

### Sintaxe

Um método pode ser declarado informando seu modificador de acesso, tipo de retorno, nome e parâmetros:

```java
public void exibirInformacao() {
    System.out.println("Produto");
}
```

Um método também pode receber parâmetros e retornar um valor:

```java
public double calcularDesconto(double percentual) {
    return preco - (preco * percentual);
}
```

### Quando utilizar?

Métodos devem ser utilizados quando uma classe precisa executar uma ação ou comportamento relacionado à sua responsabilidade.

### Exemplo prático

```java
public class Produto {

    private double preco;

    public double calcularDesconto(double percentual) {
        return preco - (preco * percentual);
    }
}
```

Nesse exemplo, `calcularDesconto()` representa um comportamento relacionado ao produto.

### Erros comuns

* Criar métodos que executam responsabilidades que pertencem a outra classe.
* Criar métodos muito grandes e com muitas responsabilidades.
* Confundir parâmetros com atributos.
* Criar métodos sem considerar a responsabilidade da classe.

### Relação com outros conceitos

Métodos representam comportamentos dos objetos e podem utilizar os atributos da própria classe.

---

## 5. Encapsulamento

### Conceito

Encapsulamento é o princípio de organizar uma classe de forma que seus dados internos não sejam acessados ou modificados diretamente de qualquer lugar do sistema.

O acesso aos dados pode ser controlado por métodos definidos pela própria classe.

### Sintaxe

Uma forma comum de aplicar encapsulamento em Java é utilizar atributos `private` e métodos para controlar seu acesso:

```java
public class Produto {

    private double preco;

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }
}
```

### Quando utilizar?

O encapsulamento deve ser utilizado quando queremos controlar como os dados de um objeto podem ser acessados ou modificados.

### Exemplo prático

Um produto não deveria necessariamente permitir que qualquer parte do sistema alterasse seu preço sem nenhuma regra.

Podemos centralizar essa alteração em um método:

```java
public void alterarPreco(double novoPreco) {
    if (novoPreco > 0) {
        this.preco = novoPreco;
    }
}
```

Dessa forma, a própria classe pode controlar a alteração do seu estado.

### Erros comuns

* Acreditar que encapsulamento significa apenas criar getters e setters.
* Tornar todos os atributos `public`.
* Permitir alterações de estado sem considerar regras relacionadas ao objeto.

### Relação com outros conceitos

O encapsulamento está relacionado aos modificadores de acesso, principalmente `private`, e aos métodos utilizados para controlar o acesso ao estado do objeto.

---

## 6. Níveis de acesso

### Conceito

Os modificadores de acesso determinam **onde uma classe, atributo ou método pode ser acessado**.

Os principais níveis de acesso em Java são `public`, `private`, `protected` e o acesso padrão, também conhecido como package-private.

### `public`

Um membro `public` pode ser acessado a partir de outras classes, desde que a classe esteja acessível.

**Exemplo:**

```java
public void exibirProduto() {
    System.out.println("Produto");
}
```

### `private`

Um membro `private` pode ser acessado diretamente apenas dentro da própria classe.

**Exemplo:**

```java
private double preco;
```

### `protected`

Um membro `protected` pode ser acessado dentro do mesmo pacote e também por classes que possuem relação de herança, respeitando as regras de acesso do Java.

**Exemplo:**

```java
protected String nome;
```

### Package-private

Quando nenhum modificador de acesso é declarado, o membro possui acesso de pacote.

**Exemplo:**

```java
String nome;
```

Nesse caso, o acesso é permitido para classes do mesmo pacote, respeitando as regras do Java.

### Quando utilizar cada um?

A escolha depende da necessidade de acesso ao membro.

* `private`: quando o acesso deve ficar restrito à própria classe.
* `public`: quando o recurso precisa ser disponibilizado para outras partes do sistema.
* `protected`: quando o acesso precisa considerar classes do mesmo pacote ou relações de herança.
* package-private: quando o recurso deve ser acessível dentro do mesmo pacote.

### Erros comuns

* Utilizar `public` para todos os atributos.
* Confundir `protected` com `public`.
* Não entender a diferença entre acesso dentro da classe, pacote e herança.

### Relação com outros conceitos

Os modificadores de acesso são importantes para aplicar encapsulamento e controlar a exposição dos membros de uma classe.

---

## 7. Herança

### Conceito

Herança permite que uma classe seja criada a partir de outra classe, podendo reutilizar características e comportamentos da classe base.

A classe que herda é chamada de subclasse e a classe da qual ela herda é chamada de superclasse.

### Sintaxe

Em Java, a palavra-chave `extends` é utilizada para indicar herança:

```java
public class Animal {

    public void emitirSom() {
        System.out.println("Som");
    }
}
```

```java
public class Cachorro extends Animal {

}
```

Nesse exemplo, `Cachorro` herda de `Animal`.

### Quando utilizar?

Herança pode ser utilizada quando existe uma relação clara de especialização entre as classes.

Por exemplo:

```text
Animal
  ↓
Cachorro
```

O cachorro é um tipo de animal, portanto pode existir uma relação de herança.

### Exemplo prático

```java
public class Animal {

    public void comer() {
        System.out.println("Comendo");
    }
}
```

```java
public class Cachorro extends Animal {

    public void latir() {
        System.out.println("Au au");
    }
}
```

Um objeto `Cachorro` pode utilizar o comportamento herdado de `Animal` e também seu próprio comportamento.

### Erros comuns

* Utilizar herança apenas para reutilizar código.
* Criar hierarquias de herança desnecessariamente complexas.
* Não verificar se realmente existe uma relação de especialização entre as classes.

### Relação com outros conceitos

Herança está relacionada à POO e pode ser utilizada junto com sobrescrita de métodos e polimorfismo.

---

## 8. Interfaces

### Conceito

Uma interface define um contrato que uma classe pode implementar.

Ela permite estabelecer quais comportamentos uma classe deve fornecer sem determinar necessariamente toda a implementação desses comportamentos.

### Sintaxe

Uma interface pode ser declarada utilizando `interface`:

```java
public interface Pagamento {

    void pagar();
}
```

Uma classe pode implementar essa interface utilizando `implements`:

```java
public class PagamentoPix implements Pagamento {

    @Override
    public void pagar() {
        System.out.println("Pagamento realizado via PIX");
    }
}
```

### Quando utilizar?

Interfaces podem ser utilizadas quando diferentes classes precisam seguir um mesmo contrato ou quando queremos diminuir o acoplamento entre partes do sistema.

### Exemplo prático

Imagine diferentes formas de pagamento:

```text
Pagamento
├── PagamentoPix
├── PagamentoCartao
└── PagamentoBoleto
```

Todas podem implementar a mesma interface:

```java
public interface Pagamento {

    void pagar();
}
```

Cada implementação pode definir seu próprio comportamento.

### Erros comuns

* Pensar que uma interface é simplesmente uma classe.
* Criar interfaces sem uma necessidade clara.
* Confundir `extends` com `implements`.
* Utilizar interfaces apenas por obrigação, sem entender o contrato que elas representam.

### Relação com outros conceitos

Interfaces estão relacionadas à abstração, polimorfismo e baixo acoplamento.

---

## 9. Relação entre os conceitos

Os conceitos de POO estão relacionados.

Uma **classe** define uma estrutura. A partir dela podemos criar **objetos**.

Os objetos possuem **atributos**, que representam seus dados, e **métodos**, que representam seus comportamentos.

O **encapsulamento** permite controlar o acesso aos dados e comportamentos da classe.

A **herança** permite estabelecer relações entre classes.

As **interfaces** permitem definir contratos que diferentes classes podem implementar.

Os **modificadores de acesso** ajudam a controlar a exposição dos elementos da classe.

---

## 10. Situação prática

Imagine um sistema de vendas.

Podemos representar diferentes elementos do sistema utilizando classes:

```text
Cliente
Produto
Pedido
Pagamento
```

Um `Produto` pode possuir:

```text
nome
preco
quantidadeEstoque
```

E comportamentos como:

```text
calcularDesconto()
baixarEstoque()
```

Um `Pedido` pode possuir informações relacionadas aos produtos comprados e comportamentos relacionados ao processamento do pedido.

Para representar diferentes formas de pagamento, podemos utilizar uma interface:

```text
Pagamento
├── PagamentoPix
├── PagamentoCartao
└── PagamentoBoleto
```

Assim, os conceitos de classes, objetos, atributos, métodos, encapsulamento e interfaces podem aparecer juntos em uma aplicação real.

---

## 11. Dúvidas e erros comuns de iniciantes

Algumas dúvidas comuns sobre POO são:

* Qual é a diferença entre classe e objeto?
* Qual é a diferença entre atributo e método?
* Para que serve `private`?
* Qual é a diferença entre `extends` e `implements`?
* Quando devo utilizar herança?
* Quando devo utilizar uma interface?
* Encapsulamento significa apenas utilizar getters e setters?
* Por que não deixar todos os atributos `public`?

Um erro comum é aprender a sintaxe sem compreender o motivo pelo qual o conceito existe.

Por isso, é importante relacionar a sintaxe com o problema que ela resolve.

---

## 12. Resumo

Programação Orientada a Objetos é uma forma de organizar programas utilizando objetos que possuem dados e comportamentos.

Os principais conceitos abordados são:

* **Classe:** define a estrutura de um tipo de objeto.
* **Objeto:** instância de uma classe.
* **Atributo:** representa dados ou características.
* **Método:** representa comportamentos.
* **Encapsulamento:** controla o acesso ao estado e aos comportamentos.
* **Modificadores de acesso:** controlam onde elementos podem ser acessados.
* **Herança:** permite estabelecer relações de especialização entre classes.
* **Interface:** define um contrato que pode ser implementado por diferentes classes.

A POO deve ser compreendida não apenas pela sintaxe, mas também pelo **problema que cada conceito ajuda a resolver e pela forma como os conceitos se relacionam em uma aplicação real**.
