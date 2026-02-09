# Árvore Binária de Busca (BST) em Python

## 📚 Índice
- [Conceitos Teóricos](#conceitos-teóricos)
- [Propriedades e Complexidade](#propriedades-e-complexidade)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Uso](#instalação-e-uso)
- [Operações Implementadas](#operações-implementadas)
- [Exemplos](#exemplos)
- [Estruturas de Dados Utilizadas](#estruturas-de-dados-utilizadas-e-justificativas-de-design)
- [Aplicações Práticas](#aplicações-práticas-de-bst)

---

## 🎓 Conceitos Teóricos

### O que é uma Árvore Binária?

Uma **árvore binária** é uma estrutura de dados hierárquica onde cada nó possui **no máximo dois filhos**: um filho esquerdo e um filho direito. O nó superior é chamado de **raiz**, e os nós sem filhos são chamados de **folhas**.

```
Exemplo de Árvore Binária:
        10
       /  \
      5    15
     / \   / \
    3   7 12  20
```

### O que é uma Árvore Binária de Busca (BST)?

Uma **BST (Binary Search Tree)** é uma árvore binária com uma propriedade adicional importante:

> **Propriedade BST**: Para cada nó, todos os valores na **subárvore esquerda** são **menores** que o valor do nó, e todos os valores na **subárvore direita** são **maiores** que o valor do nó.

```
Exemplo de BST:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

- Todos à esquerda de 50: 30, 20, 40 (menores)
- Todos à direita de 50: 70, 60, 80 (maiores)
```

### Diferenças entre Estruturas de Árvores

| Estrutura | Propriedade Principal | Uso Comum |
|-----------|----------------------|-----------|
| **Árvore Binária** | Máximo 2 filhos por nó | Base para outras estruturas |
| **BST** | Valores ordenados (esq < raiz < dir) | Busca eficiente, dicionários |
| **Árvore AVL** | BST auto-balanceada (altura equilibrada) | Garantir O(log n) sempre |
| **Árvore Red-Black** | BST balanceada com cores nos nós | Map/Set em linguagens |
| **Heap** | Pai maior/menor que filhos (não ordenada) | Fila de prioridade |
| **Árvore B** | Múltiplos filhos por nó | Bancos de dados, sistemas de arquivos |

### Por que usar uma BST?

**Vantagens:**
- Busca eficiente em árvores balanceadas: O(log n)
- Inserção e remoção relativamente rápidas
- Percurso in-order produz valores em ordem crescente
- Fácil de implementar e entender

**Desvantagens:**
- Pode degenerar em lista ligada (pior caso O(n))
- Não garante balanceamento automático
- Desempenho depende da ordem de inserção

---

## 📊 Propriedades e Complexidade

### Complexidade de Tempo

| Operação | Melhor Caso | Caso Médio | Pior Caso |
|----------|-------------|------------|-----------|
| **Busca** | O(log n) | O(log n) | O(n) |
| **Inserção** | O(log n) | O(log n) | O(n) |
| **Remoção** | O(log n) | O(log n) | O(n) |
| **Percurso** | O(n) | O(n) | O(n) |

**Onde:**
- **n** = número de nós na árvore
- **h** = altura da árvore
- **Melhor caso**: Árvore perfeitamente balanceada (h = log n)
- **Pior caso**: Árvore degenerada em lista (h = n)

### Exemplo de Degeneração

```
Inserindo valores em ordem crescente: 1, 2, 3, 4, 5

Árvore resultante (degenerada):
1
 \
  2
   \
    3
     \
      4
       \
        5

Altura = 5 (igual ao número de nós)
Busca por 5: 5 comparações (O(n))
```

```
Inserindo valores balanceados: 3, 1, 4, 2, 5

Árvore resultante (balanceada):
    3
   / \
  1   4
   \   \
    2   5

Altura = 3 (log₂(5) ≈ 2.3)
Busca por 5: 2 comparações (O(log n))
```

### Balanceamento

Uma árvore é considerada **balanceada** quando a diferença de altura entre as subárvores esquerda e direita de qualquer nó é **no máximo 1**.

```
Balanceada:              Não Balanceada:
      10                       10
     /  \                     /
    5    15                  5
   / \                      /
  3   7                    3
                          /
                         1

Diferença: |2-1| = 1     Diferença: |3-0| = 3
✓ Balanceada             ✗ Não Balanceada
```

---

## 📁 Estrutura do Projeto

```
arvore binaria/
├── arvore_binaria.py           # Arquivo principal (menu interativo)
├── requirements.txt            # Dependências (matplotlib)
├── arvores_bst.json           # Árvores salvas (persistência)
├── README.md                  # Esta documentação
└── funcoes/                   # Módulo com todas as funções
    ├── __init__.py
    ├── node.py                # Classe Node
    ├── validacao.py           # Validação de entrada
    ├── inserir.py             # Operações de inserção
    ├── buscar.py              # Operação de busca
    ├── remover.py             # Operação de remoção
    ├── operacoes_auxiliares.py # Min, max, altura, tamanho
    ├── percursos.py           # Traversals (in-order, pre-order, etc)
    ├── salvar_carregar_arvore.py # Persistência JSON
    └── plotar_arvore.py       # Visualização com matplotlib
```

---

## 🚀 Instalação e Uso

### Pré-requisitos

- **Python 3.10+** (necessário para sintaxe `match-case`)
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd arvore\ binaria/
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executar o Programa

```bash
python arvore_binaria.py
```

---

## 🔧 Operações Implementadas

### Menu Principal (6 opções)

1. **Inserir valores**
   - Insere um ou múltiplos valores (separados por vírgula)
   - Valida entrada (apenas inteiros, sem duplicados)
   - Mantém propriedade BST

2. **Buscar valor**
   - Retorna se o valor existe na árvore
   - Mostra o caminho percorrido durante a busca
   - Permite visualização com destaque do caminho

3. **Remover valor**
   - Remove nó mantendo propriedade BST
   - Três casos: sem filhos, um filho, dois filhos
   - Feedback com mensagens claras

4. **Visualizar árvore**
   - Gráfico matplotlib com posicionamento hierárquico
   - Destaque de caminho de busca (opcional)

5. **Info (Estatísticas + Percursos)**
   - Tamanho, altura, mínimo, máximo
   - Verificação de balanceamento
   - Percursos In-Order e Level-Order

6. **Gerenciar (Submenu)**
   - Salvar árvore com nome personalizado
   - Carregar árvore salva
   - Listar árvores disponíveis
   - Limpar árvore atual

### 🔒 Salvamento Automático

- **Auto-save ao sair**: Árvore é salva automaticamente quando você fecha o programa
- **Auto-load ao iniciar**: Árvore anterior é carregada automaticamente na próxima execução
- **Arquivo**: `_auto_save_` (oculto da listagem de árvores salvas)

---

## 💡 Exemplos

### Exemplo 1: Inserção Básica

```
Inserindo: 50, 30, 70, 20, 40, 60, 80

Árvore resultante:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

In-order: 20, 30, 40, 50, 60, 70, 80 (ordem crescente)
Altura: 2
Tamanho: 7 nós
Balanceada: Sim
```

### Exemplo 2: Busca com Caminho

```
Buscar valor 40 na árvore acima:

Caminho percorrido:
50 → 30 → 40

Visualização:
        50 (amarelo - visitado)
       /  \
      30   70
     / \   / \
    20 40 60 80
    (verde - encontrado!)

Comparações: 3
Encontrado: Sim
```

### Exemplo 3: Remoção (Dois Filhos)

```
Remover 30 da árvore:

Antes:              Depois:
      50                  50
     /  \                /  \
    30   70             40   70
   / \   / \           /    / \
  20 40 60 80        20   60 80

Processo:
1. Encontrar sucessor in-order (menor valor da subárvore direita): 40
2. Substituir valor de 30 por 40
3. Remover nó 40 original (caso simples: sem filhos)
```

### Exemplo 4: Percurso Level-Order (BFS com Deque)

```
Árvore:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Percurso Level-Order (por níveis):
50 → 30 → 70 → 20 → 40 → 60 → 80

Processo com deque:
1. Inicia: fila = deque([50])
2. Processa 50: fila.popleft() O(1), adiciona filhos
   fila = deque([30, 70])
3. Processa 30: fila.popleft() O(1), adiciona filhos
   fila = deque([70, 20, 40])
4. Processa 70: fila.popleft() O(1), adiciona filhos
   fila = deque([20, 40, 60, 80])
... continua até esvaziar
```

---

## 📖 Estruturas de Dados Utilizadas e Justificativas de Design

### Recursão
A maioria das operações em BST usa **recursão** para percorrer a árvore:
- Caso base: nó é None
- Caso recursivo: processa subárvore esquerda/direita

### Backtracking
Usado na busca e remoção para voltar na árvore quando necessário.

---

### Estruturas Auxiliares e Escolhas de Design

#### 🔍 Persistência com **Dicionário (dict)** para Serialização JSON

Um dos grandes desafios ao trabalhar com qualquer estrutura de dados em memória é conseguir armazená-la de forma durável. Neste projeto, enfrentamos esse desafio ao implementar a funcionalidade de salvar e carregar árvores em arquivo JSON. A questão central é: como converter uma árvore de nós (objetos Python em memória) para um formato que possa ser armazenado em disco e recriado posteriormente?

A resposta natural é usar **dicionários aninhados** como intermediários. A hierarquia de uma árvore binária mapeia-se de forma orgânica para a estrutura de dicionários recursivos do Python. Cada nó torna-se um dicionário contendo seu valor e referências para seus filhos, que são, por sua vez, outros dicionários (ou `None` para ausência de filho).

```python
# Árvore em memória (usando objetos Node):
#        50
#       /  \
#      30   70

# Representação com dicionários (pronta para JSON):
arvore_dict = {
    "valor": 50,
    "left": {
        "valor": 30,
        "left": None,
        "right": None
    },
    "right": {
        "valor": 70,
        "left": None,
        "right": None
    }
}
```

Por que essa abordagem é superior a alternativas? Primeiro, o Python e JSON compartilham uma compatibilidade natural com dicionários—não é necessário fazer conversões intermediárias complicadas. Segundo, essa estrutura é **autoexplicativa**: qualquer pessoa lendo o JSON pode imediatamente entender que cada nó possui um valor e dois filhos (esquerdo e direito). Essa clareza reduz erros na implementação.

Além disso, usar dicionários permite **estender facilmente os metadados** sem quebrar a estrutura. Por exemplo, podemos adicionar informações sobre quando a árvore foi salva, qual seu tamanho, ou seu nível de balanceamento—tudo isso sem comprometer a serialização:

```python
arvore_completa = {
    "nome": "arvore_vendas",
    "data_criacao": "2026-02-05",
    "altura": 3,
    "tamanho": 7,
    "raiz": { ... }  # A árvore propriamente dita
}
```

Alternativas como listas (`[50, [30, None, None], [70, None, None]]`) de fato são mais compactas em memória, mas sacrificam a legibilidade—qual índice representa qual filho? Essa ambiguidade leva a erros. Tuplas têm o mesmo problema agravado pela imutabilidade. Em contraste, a abordagem com dicionários sacrifica um pouco de memória em nome da clareza e da manutenibilidade, um trade-off muito apropriado para um projeto educacional.

---

#### 🚄 Percurso em Largura com **Deque (Fila)** para Eficiência

Quando implementamos um percurso de nível por nível (BFS - Breadth-First Search), precisamos processar nós em ordem FIFO: primeiro a entrar deve ser o primeiro a sair. A escolha de estrutura aqui parece trivial, mas tem implicações profundas de performance.

O percurso utiliza uma fila para manter os nós a visitar. Começamos com a raiz e, conforme processamos cada nó, adicionamos seus filhos ao final da fila. A operação crítica é **remover nós do início da fila**—precisamos fazer isso repetidamente, uma vez para cada nó na árvore.

Python oferece duas estruturas óbvias para implementar essa fila: `list` e `deque`. À primeira vista, parecem equivalentes—ambas suportam adição e remoção. Porém, a diferença no desempenho é dramática quando se trata de remover do início.

```python
# ❌ Implementação com list (ineficiente):
from collections import deque

def percurso_level_order_lista(raiz):
    fila = [raiz]  # Usa list
    resultado = []
    
    while fila:
        node = fila.pop(0)  # PROBLEMA: O(n) no pior caso!
        resultado.append(node.valor)
        
        if node.left:
            fila.append(node.left)
        if node.right:
            fila.append(node.right)
    
    return resultado

# ✅ Implementação com deque (eficiente):
def percurso_level_order(raiz):
    fila = deque([raiz])  # Usa deque
    resultado = []
    
    while fila:
        node = fila.popleft()  # ✓ O(1) sempre
        resultado.append(node.valor)
        
        if node.left:
            fila.append(node.left)
        if node.right:
            fila.append(node.right)
    
    return resultado
```

Por quê a diferença? Quando você remove o primeiro elemento de uma `list` em Python, você força o reindexação de **todos os elementos restantes**—é como tirar a primeira carta do topo de um baralho espalhado na mesa e depois reorganizar todas as cartas. Com `deque` (double-ended queue), a remoção do início é uma simples operação de ponteiro, sem reindexação necessária.

Para uma árvore pequena com 10 nós, essa diferença é imperceptível. Mas considere uma árvore balanceada com 1000 nós: a implementação com `list` executa aproximadamente 500 mil operações de movimentação de elementos, enquanto `deque` executa 1000 simples remoções. **A diferença é de 500 vezes mais lento**. Para árvores ainda maiores, essa diferença é catastrófica.

Este é exatamente o tipo de decisão que separa código que "funciona" de código que **escala bem**. Por isso, neste projeto, utilizamos `deque` para qualquer operação que exija remoção frequente do início de uma coleção.

---

#### 📍 Rastreamento de Caminho com **Lista** para Busca

Quando buscamos um valor na árvore, queremos não apenas saber se ele existe, mas também **registrar o caminho percorrido**. Isso permite visualizar no gráfico qual foi a rota de busca e oferece ao usuário uma compreensão clara de como o algoritmo explorou a árvore.

Para isso, utilizamos uma `list` simples. A razão é prática: durante a busca (que segue um caminho linear até encontrar o nó ou chegar a None), adicionamos incrementalmente cada nó visitado ao final da lista. Essa operação de `append()` é muito eficiente—não precisamos remover elementos do início, apenas adicionar ao final.

```python
def buscar_com_caminho(raiz, valor):
    caminho = []  # Lista acumula os nós visitados
    atual = raiz
    
    while atual:
        caminho.append(atual.valor)  # O(1) amortizado
        
        if valor == atual.valor:
            return (True, caminho)
        elif valor < atual.valor:
            atual = atual.left
        else:
            atual = atual.right
    
    return (False, caminho)
```

Por que `list` aqui é a escolha correta? Primeiro, fazemos apenas `append()`, nunca `popleft()`, então não há penalidade de performance. Segundo, frequentemente precisamos acessar o caminho depois para visualizar—`list` oferece acesso aleatório O(1), enquanto outras estruturas poderiam ser menos convenientes. Terceiro, simplicidade: `list` é a ferramenta mais comum do Python, sem necessidade de importar `deque`. 

Essa é uma lição importante sobre design: não escolha estruturas apenas porque são "mais eficientes em teoria". Escolha a estrutura que resolve seu problema específico de forma simples e clara. Neste caso, `list` resolve de forma perfeita.

#### 🔑 Síntese: Estruturas de Dados e Suas Funções

Ao longo do projeto, vemos que **a escolha da estrutura de dados não é um detalhe técnico abstrato, mas uma decisão que diretamente impacta a clareza do código, a facilidade de manutenção e o desempenho da aplicação**. Utilizamos `dict` para persistência porque ele expressa naturalmente a hierarquia de uma árvore e integra-se perfeitamente com JSON. Utilizamos `deque` para o percurso em largura porque a operação fundamental (remoção do início) exige uma estrutura que não force reindexação. E utilizamos `list` para rastreamento de caminho porque o padrão de acesso (apenas adições ao final) torna-a ideal em simplicidade e performance.

Essa combinação de estruturas cada uma escolhida para seu uso específico resulta em um projeto que não apenas funciona, mas que **comunica claramente a intenção do programador** ao próximo estudante que ler o código.

---

#### 🎨 Visualização Hierárquica com **Matplotlib**

Um aspecto crucial para a compreensão de estruturas de dados como árvores é poder **visualizá-las graficamente**. Neste projeto, utilizamos a biblioteca **Matplotlib** para renderizar a árvore binária de forma clara e intuitiva, transformando nós e arestas abstratos em um diagrama visual que qualquer pessoa pode entender imediatamente.

O desafio da visualização de árvores é **posicionar corretamente cada nó no plano 2D** mantendo a hierarquia visual clara. Uma estratégia comum é usar uma abordagem **recursiva por níveis**: colocamos a raiz no topo, os nós do segundo nível abaixo dela com espaçamento apropriado, e assim sucessivamente. Esta distribuição "em camadas" reflete naturalmente a estrutura da árvore.

**Por que Matplotlib?** Existem várias bibliotecas de visualização em Python—Plotly, Bokeh, Graphviz—mas Matplotlib é a escolha ideal para este projeto educacional porque:

- **Simplicidade**: Matplotlib é direto e didático, sem abstrações complicadas
- **Controle fino**: Você desenha literalmente cada elemento (nó, arestas, cores) na tela
- **Distribuição padrão**: Já vem com praticamente qualquer instalação Python
- **Feedback imediato**: As renderizações aparecem rapidamente sem compilações intermediárias
- **Documentação excelente**: Milhões de exemplos e tutoriais disponíveis

Durante a busca, o Matplotlib oferece um recurso particularmente valioso: podemos **destacar visualmente o caminho percorrido** colorindo os nós visitados em amarelo e o nó encontrado em verde. Isso transforma a busca de uma operação abstrata em um processo visual que o estudante pode acompanhar e compreender intuitivamente.

```python
# Exemplo: buscamos 40 na árvore
#        50 (amarelo - visitado)
#       /  \
#      30   70  (30 amarelo - visitado)
#     / \   / \
#    20 40 60 80  (40 verde - encontrado!)

# Matplotlib renderiza cada nó com sua cor apropriada
# e traça linhas conectando pais aos filhos
```

Essa visualização interativa é fundamental em um projeto educacional: ver é compreender. A árvore deixa de ser uma abstração de memória e becomes um objeto tangível na tela.

---

## 🎯 Aplicações Práticas de BST

1. **Dicionários e conjuntos ordenados**: Manter elementos em ordem
2. **Bancos de dados**: Índices para busca rápida
3. **Autocompletar**: Sugestões baseadas em prefixos
4. **Roteamento de rede**: Tabelas de roteamento
5. **Compressão de dados**: Base para árvores de Huffman
6. **Sistemas de arquivos**: Hierarquia de diretórios

---

## 👨‍🎓 Autor

Desenvolvido como projeto educacional para disciplina de Estrutura de Dados.

---

## 📄 Licença

Este projeto é de código aberto para fins educacionais.


