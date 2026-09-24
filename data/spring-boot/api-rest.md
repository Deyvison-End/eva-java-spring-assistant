# API REST com Spring Boot

## 1. O que é uma API?

### Conceito

API significa **Application Programming Interface**.

Uma API permite que diferentes sistemas ou aplicações se comuniquem por meio de uma interface definida.

Em uma aplicação web, uma API pode receber uma requisição de um cliente, processar essa requisição e retornar uma resposta.

Por exemplo:

```text
Aplicação cliente
       ↓
    Requisição
       ↓
      API
       ↓
   Processamento
       ↓
     Resposta
       ↓
Aplicação cliente
```

### Para que serve?

Uma API pode permitir que diferentes aplicações compartilhem informações e funcionalidades.

Por exemplo, uma aplicação frontend pode utilizar uma API para:

* cadastrar usuários;
* consultar produtos;
* atualizar informações;
* excluir registros;
* realizar autenticação.

### Quando utilizar?

Uma API é utilizada quando diferentes partes de um sistema precisam se comunicar ou quando queremos disponibilizar funcionalidades e dados para outras aplicações.

---

# 2. O que é REST?

### Conceito

REST significa **Representational State Transfer**.

REST é um estilo arquitetural utilizado para projetar sistemas que se comunicam por meio de recursos.

Em uma API REST, os recursos são normalmente identificados por URLs e manipulados utilizando os métodos HTTP.

Por exemplo:

```text
/produtos
/clientes
/pedidos
```

Cada endereço representa um recurso da aplicação.

### Para que serve?

REST fornece uma forma padronizada de estruturar a comunicação entre cliente e servidor utilizando conceitos do protocolo HTTP.

### Quando utilizar?

REST é utilizado frequentemente na construção de APIs web que precisam permitir que diferentes clientes consumam recursos de uma aplicação.

---

# 3. API REST

### Conceito

Uma API REST é uma API projetada seguindo princípios do estilo arquitetural REST e utilizando HTTP para comunicação.

Uma API REST normalmente utiliza métodos HTTP para indicar a operação que será realizada sobre um recurso.

```text
GET     → consultar
POST    → criar
PUT     → atualizar
DELETE  → remover
```

### Exemplo prático

Para um recurso `produto`, podemos ter:

```text
GET     /produtos
POST    /produtos
GET     /produtos/1
PUT     /produtos/1
DELETE  /produtos/1
```

A URL representa o recurso e o método HTTP indica a operação.

### Erros comuns

* Confundir uma URL com o método HTTP.
* Utilizar `POST` para todas as operações.
* Não diferenciar o recurso da ação realizada sobre ele.

---

# 4. `@RestController`

### Conceito

`@RestController` é uma anotação do Spring utilizada para indicar que uma classe atua como um controlador de uma API REST.

Ela permite que a classe receba requisições HTTP e produza respostas que serão enviadas ao cliente.

### Sintaxe

```java
@RestController
@RequestMapping("/produtos")
public class ProdutoController {

}
```

### Quando utilizar?

Utilizamos `@RestController` em classes responsáveis por receber e responder requisições HTTP de uma API REST.

### Exemplo prático

```java
@RestController
@RequestMapping("/produtos")
public class ProdutoController {

    @GetMapping
    public String listarProdutos() {
        return "Lista de produtos";
    }
}
```

Uma requisição:

```text
GET /produtos
```

pode ser direcionada para o método `listarProdutos()`.

### Erros comuns

* Colocar toda a lógica de negócio dentro do controller.
* Confundir controller com service.
* Não definir corretamente o caminho dos endpoints.

### Relação com outros conceitos

`@RestController` está relacionado aos métodos HTTP e às outras anotações de mapeamento, como `@GetMapping`, `@PostMapping`, `@PutMapping` e `@DeleteMapping`.

---

# 5. `@RequestMapping`

### Conceito

`@RequestMapping` permite definir o caminho ou outras características de uma requisição HTTP.

Pode ser utilizado na classe para definir um caminho base para os endpoints.

### Sintaxe

```java
@RestController
@RequestMapping("/produtos")
public class ProdutoController {

}
```

Nesse exemplo, `/produtos` é o caminho base do controller.

### Quando utilizar?

Pode ser utilizado para definir o caminho base de um conjunto de endpoints ou para realizar mapeamentos mais específicos.

### Exemplo prático

```java
@RestController
@RequestMapping("/produtos")
public class ProdutoController {

    @GetMapping
    public String listar() {
        return "Produtos";
    }
}
```

O endpoint será:

```text
GET /produtos
```

### Erros comuns

* Confundir `@RequestMapping` com `@GetMapping`.
* Criar caminhos inconsistentes para os recursos.
* Não entender que um `@RequestMapping` na classe pode servir como caminho base.

### Relação com outros conceitos

`@RequestMapping` pode ser utilizado junto com as anotações específicas dos métodos HTTP.

---

# 6. `@GetMapping`

### Conceito

`@GetMapping` é utilizado para mapear requisições HTTP `GET`.

O método `GET` é normalmente utilizado para consultar recursos.

### Sintaxe

```java
@GetMapping
public String listar() {
    return "Lista de produtos";
}
```

### Quando utilizar?

Utilize `@GetMapping` quando o endpoint tiver como objetivo consultar ou obter informações.

### Exemplo prático

```java
@GetMapping("/produtos")
public List<Produto> listarProdutos() {
    return produtoService.listarTodos();
}
```

Uma requisição:

```text
GET /produtos
```

solicita a lista de produtos.

### Erros comuns

* Utilizar `GET` para operações que alteram dados.
* Confundir consulta de todos os recursos com consulta de um recurso específico.

### Relação com outros conceitos

`@GetMapping` faz parte do conjunto de mapeamentos HTTP do Spring:

```text
@GetMapping
@PostMapping
@PutMapping
@DeleteMapping
```

---

# 7. `@PostMapping`

### Conceito

`@PostMapping` é utilizado para mapear requisições HTTP `POST`.

O método `POST` é normalmente utilizado para criar um novo recurso.

### Sintaxe

```java
@PostMapping
public Produto cadastrar(@RequestBody Produto produto) {
    return produtoService.cadastrar(produto);
}
```

### Quando utilizar?

Utilize `@PostMapping` quando a operação tiver como objetivo criar ou enviar dados para processamento no servidor.

### Exemplo prático

```java
@PostMapping
public Produto cadastrar(@RequestBody Produto produto) {
    return produtoService.cadastrar(produto);
}
```

Uma requisição pode enviar:

```json
{
    "nome": "Notebook",
    "preco": 3500.00
}
```

### Erros comuns

* Utilizar `POST` para consultas simples.
* Não utilizar `@RequestBody` quando os dados são enviados no corpo da requisição e precisam ser convertidos para um objeto.
* Colocar regras de negócio diretamente no controller.

### Relação com outros conceitos

`@PostMapping` frequentemente aparece junto com `@RequestBody` em endpoints de criação.

---

# 8. `@PutMapping`

### Conceito

`@PutMapping` é utilizado para mapear requisições HTTP `PUT`.

É normalmente utilizado para atualizar um recurso existente.

### Sintaxe

```java
@PutMapping("/{id}")
public Produto atualizar(
        @PathVariable Integer id,
        @RequestBody Produto produto) {

    return produtoService.atualizar(id, produto);
}
```

### Quando utilizar?

Utilize `@PutMapping` quando o objetivo do endpoint for atualizar um recurso existente.

### Exemplo prático

```text
PUT /produtos/10
```

O `10` identifica o produto que será atualizado.

O corpo da requisição pode conter os novos dados:

```json
{
    "nome": "Notebook Gamer",
    "preco": 5000.00
}
```

### Erros comuns

* Confundir `PUT` com `POST`.
* Não utilizar o identificador do recurso quando necessário.
* Colocar regras de atualização diretamente no controller.

### Relação com outros conceitos

`@PutMapping` frequentemente utiliza `@PathVariable` para identificar o recurso e `@RequestBody` para receber os dados.

---

# 9. `@DeleteMapping`

### Conceito

`@DeleteMapping` é utilizado para mapear requisições HTTP `DELETE`.

É normalmente utilizado para remover um recurso.

### Sintaxe

```java
@DeleteMapping("/{id}")
public void excluir(@PathVariable Integer id) {
    produtoService.excluir(id);
}
```

### Quando utilizar?

Utilize `@DeleteMapping` quando o endpoint tiver como objetivo remover um recurso.

### Exemplo prático

```text
DELETE /produtos/10
```

Nesse caso, o produto identificado pelo ID `10` será enviado para a operação de exclusão.

### Erros comuns

* Utilizar `DELETE` para operações que não representam remoção.
* Não identificar corretamente o recurso que será removido.
* Colocar toda a regra de exclusão no controller.

### Relação com outros conceitos

`@DeleteMapping` pode utilizar `@PathVariable` para identificar o recurso que será removido.

---

# 10. `@PathVariable`

### Conceito

`@PathVariable` permite obter um valor que faz parte da própria URL da requisição.

### Sintaxe

```java
@GetMapping("/{id}")
public Produto buscar(@PathVariable Integer id) {
    return produtoService.buscarPorId(id);
}
```

### Quando utilizar?

É utilizado quando uma informação faz parte da identificação do recurso na URL.

### Exemplo prático

Requisição:

```text
GET /produtos/10
```

O valor `10` pode ser obtido através de:

```java
@PathVariable Integer id
```

### Erros comuns

* Confundir `@PathVariable` com `@RequestParam`.
* Fazer o nome da variável Java não corresponder ao nome definido no caminho quando não houver configuração explícita.

### Relação com outros conceitos

É frequentemente utilizado em operações sobre um recurso específico:

```text
GET /produtos/{id}
PUT /produtos/{id}
DELETE /produtos/{id}
```

---

# 11. `@RequestParam`

### Conceito

`@RequestParam` permite obter parâmetros enviados na URL como parâmetros de consulta.

### Sintaxe

```java
@GetMapping
public List<Produto> buscarPorNome(
        @RequestParam String nome) {

    return produtoService.buscarPorNome(nome);
}
```

### Quando utilizar?

É utilizado principalmente para filtros, buscas, paginação ou outros parâmetros opcionais da consulta.

### Exemplo prático

Requisição:

```text
GET /produtos?nome=Notebook
```

O valor `Notebook` pode ser recebido por:

```java
@RequestParam String nome
```

### Erros comuns

* Confundir `@RequestParam` com `@PathVariable`.
* Utilizar parâmetros de consulta quando a informação deveria identificar diretamente um recurso.

### Relação com outros conceitos

`@RequestParam` é muito utilizado em endpoints de consulta e filtros.

---

# 12. `@RequestBody`

### Conceito

`@RequestBody` permite receber os dados enviados no corpo da requisição e convertê-los para um objeto Java.

### Sintaxe

```java
@PostMapping
public Produto cadastrar(@RequestBody Produto produto) {
    return produtoService.cadastrar(produto);
}
```

### Quando utilizar?

É utilizado quando o cliente precisa enviar dados no corpo da requisição, como em operações de criação e atualização.

### Exemplo prático

Requisição:

```text
POST /produtos
```

Corpo:

```json
{
    "nome": "Notebook",
    "preco": 3500.00
}
```

O Spring pode converter esses dados para um objeto `Produto`.

### Erros comuns

* Confundir dados do corpo com parâmetros da URL.
* Não compreender a relação entre JSON e o objeto Java recebido.
* Colocar validações e regras de negócio diretamente no controller.

### Relação com outros conceitos

`@RequestBody` aparece frequentemente junto com `@PostMapping` e `@PutMapping`.

---

# 13. Situação prática

Imagine uma API para gerenciamento de produtos.

Podemos definir os seguintes endpoints:

```text
GET     /produtos
GET     /produtos/{id}
POST    /produtos
PUT     /produtos/{id}
DELETE  /produtos/{id}
```

Eles representam operações diferentes sobre o recurso `produto`.

### Consultar todos

```text
GET /produtos
```

### Consultar um produto

```text
GET /produtos/10
```

### Cadastrar

```text
POST /produtos
```

```json
{
    "nome": "Notebook",
    "preco": 3500.00
}
```

### Atualizar

```text
PUT /produtos/10
```

```json
{
    "nome": "Notebook Gamer",
    "preco": 5000.00
}
```

### Excluir

```text
DELETE /produtos/10
```

Um controller pode organizar essas operações:

```java
@RestController
@RequestMapping("/produtos")
public class ProdutoController {

    @GetMapping
    public List<Produto> listar() {
        // ...
    }

    @GetMapping("/{id}")
    public Produto buscar(@PathVariable Integer id) {
        // ...
    }

    @PostMapping
    public Produto cadastrar(@RequestBody Produto produto) {
        // ...
    }

    @PutMapping("/{id}")
    public Produto atualizar(
            @PathVariable Integer id,
            @RequestBody Produto produto) {
        // ...
    }

    @DeleteMapping("/{id}")
    public void excluir(@PathVariable Integer id) {
        // ...
    }
}
```

---

# 14. Dúvidas e erros comuns de iniciantes

### "GET, POST, PUT e DELETE são anotações do Spring?"

Não.

Eles são **métodos HTTP**.

As anotações do Spring são:

```text
@GetMapping
@PostMapping
@PutMapping
@DeleteMapping
```

Essas anotações permitem mapear métodos Java para determinados métodos HTTP.

### "Qual a diferença entre `@PathVariable` e `@RequestParam`?"

`@PathVariable` obtém uma informação que faz parte do caminho:

```text
/produtos/10
```

`@RequestParam` obtém uma informação enviada como parâmetro de consulta:

```text
/produtos?nome=Notebook
```

### "Qual a diferença entre `@RequestBody` e `@RequestParam`?"

`@RequestBody` obtém dados do corpo da requisição.

`@RequestParam` obtém dados dos parâmetros da URL.

### "O controller deve fazer toda a lógica?"

Não.

O controller normalmente é responsável por receber a requisição e encaminhar a operação para componentes responsáveis pela regra de negócio.

---

# 15. Relação com outros conceitos

Uma API REST em Spring Boot normalmente utiliza vários conceitos que aparecem em outros arquivos da base:

```text
API REST
   │
   ├── @RestController
   │
   ├── @GetMapping
   ├── @PostMapping
   ├── @PutMapping
   ├── @DeleteMapping
   │
   ├── @PathVariable
   ├── @RequestParam
   └── @RequestBody
          │
          ↓
      Controller
          │
          ↓
       Service
          │
          ↓
      Repository
```

A separação entre controller, service e repository está relacionada aos conceitos de **responsabilidade, alta coesão e baixo acoplamento**.

---

# 16. Resumo

Uma API REST permite que diferentes aplicações se comuniquem utilizando HTTP.

No Spring Boot, `@RestController` é utilizado para criar controllers responsáveis por atender requisições HTTP.

Os principais mapeamentos são:

* `@GetMapping` → consultas;
* `@PostMapping` → criação/envio de dados;
* `@PutMapping` → atualização;
* `@DeleteMapping` → remoção.

Para receber informações da requisição, podemos utilizar:

* `@PathVariable` → valor presente no caminho da URL;
* `@RequestParam` → parâmetro de consulta;
* `@RequestBody` → dados enviados no corpo da requisição.

Uma API bem estruturada separa as responsabilidades entre diferentes componentes, permitindo que o controller não concentre toda a lógica da aplicação.
