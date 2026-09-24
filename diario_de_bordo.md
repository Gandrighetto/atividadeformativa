# Diário de Bordo

Este documento serve como um registro do desenvolvimento do projeto **Biblioteca de Jogos**.

## 04 de Setembro de 2026

**O que foi feito:**
- Criação do script inicial em Python com um loop infinito (`while True`) e menu interativo.
- Evolução do sistema para incluir uma **"memória"** usando uma lista (`jogos = []`).
- Implementação do comando `ADD` para receber a quantidade de jogos desejada e usar um loop `for` para salvar cada jogo na memória com o método `.append()`.
- Criação do comando `LIST` para imprimir a lista de jogos salvos enumerados, incluindo validação para avisar quando a lista estiver vazia.
- Adição da instrução `break` no comando `QUIT` para encerrar o programa corretamente.
- Renomeação do arquivo principal para `lista_jogos.py`, seguindo o padrão de nomenclatura do Python (snake_case).
- Documentação completa do projeto e das variáveis no arquivo `README.md`.
- Commits e push das alterações para o GitHub.
- Sessão de Code Review e Refatoração:
  - Substituição de `startswith("ADD")` por verificação exata `== "ADD"`.
  - Uso de `.strip()` para evitar nomes de jogos vazios ou compostos apenas por espaços.
  - Implementação da validação de lista vazia (`if not jogos:`).
  - Melhoria na legibilidade do loop `LIST` utilizando a função nativa `enumerate()`.
**Como usei a IA para melhorar meu código**
- a IA me ajudou a melhorar meu código com sugestões de melhoria, como substituir o `startswith("ADD")` por `== "ADD"`, pois o primeiro so verificava se a string começava com o comando, e o segundo verificava se a string era exatamente o comando.
- a IA me ajudou com o `strip()` que eu não sabia que existia, e com a implementação da validação de lista vazia (`if not jogos:`).
- Me ajudou tambem a substituir a range(len(jogos)) por enumerate(jogos), que é mais legivel e eficiente.
- A IA tambem me ajudou a melhorar a legibilidade do código, organização do projeto e com a criação da documentação do projeto.
- Me ajudou a entender melhor o conceito de listas, deu dicas de como prosseguir com o projeto e com a formatação padrão de código em python.
- Explicou o que significa o if __name__ == "__main__": que serve para que o código seja executado apenas quando o arquivo é executado diretamente, e não quando é importado como um módulo. Isso ajuda a organizar o código e a evitar erros.
- Corrigiu erros de portugues, gramatica e ortografia.

**Próximos passos:**
- (A definir)

## 20 de Setembro de 2026 (Atividade Formativa 2)

**O que foi feito:**
- Refatoração da memória principal (`jogos`): a lista agora armazena dicionários em vez de strings.
- Cada dicionário possui as chaves: `nome`, `concluido` (booleano), `historico` (lista de tuplas) e adicionamos `plataforma`.
- Ajuste no comando `ADD`: solicita informações via `input()`, cria o dicionário (com `concluido` False por padrão) e o adiciona à lista.
- Ajuste no comando `LIST`: exibe de forma formatada as propriedades do dicionário.
- Criação do comando `UPDATE`: busca pelo nome, permite atualização dos dados, e gera um registro (tupla) no `historico` contendo `(data, status, nome)`.
- Criação do comando `DELETE`: procura pelo dicionário correspondente e o remove da lista usando `.remove()`.

**Como usei a IA para melhorar meu código:**
- A IA me mostrou como importar e usar `datetime.now().strftime()` para gerar a data/hora automática do histórico do update.
- Me ajudou a entender como buscar um dicionário específico dentro de uma lista iterando com um loop `for` e comparando a chave desejada (ex. `jogo['nome']`).
- Explicou o uso de tuplas para os registros do histórico, visto que são imutáveis e representam um log temporal perfeito.
- Orientou no método `.remove(jogo)` para deletar um dicionário inteiro da lista.

## Refatoração com Funções (Etapa Seguinte)

**O que foi feito:**
- Refatoração do código principal da aplicação para utilizar funções, melhorando a modularização e legibilidade.
- Criação da função `encontrar_jogo(jogos, nome_jogo)` que centraliza a lógica de busca iterativa usando um loop `for` e que retorna o dicionário do jogo (se encontrado) ou `None`.
- Desmembramento das lógicas dos comandos em funções independentes: `adicionar_jogos(jogos)`, `listar_jogos(jogos)`, `atualizar_jogo(jogos)`, `remover_jogo(jogos)` e `mostrar_about()`.
- Modificação das funções de **UPDATE** e **DELETE** para aproveitarem a função `encontrar_jogo(jogos, nome)`, evitando repetição do loop de busca.
- Limpeza do loop principal em `biblioteca()`, que agora gerencia apenas as condicionais e invoca a respectira função responsável pela tarefa, passando os argumentos necessários.

## Melhorias de Boas Práticas (Code Smells)

**O que foi feito:**
- Adição de **Type Hints** nas assinaturas das funções (ex: `jogos: list[dict]`, `-> None`), explicitando os tipos de parâmetros e retornos.
- Inclusão de **Docstrings** em todas as funções documentando seus propósitos e comportamentos.
- Aplicação do padrão **Early Return** nas lógicas principais (`adicionar_jogos`, `atualizar_jogo`, `remover_jogo`), reduzindo o aninhamento (deep nesting) e validando erros precocemente.
- Substituição da extensa cadeia de `if/elif` no menu principal pela estrutura **`match / case`** (Python 3.10+), deixando o código do loop infinito limpo, escalável e direto.

**Como usei a IA para melhorar meu código:**
- Interagi com a IA assumindo um papel ("roleplay") onde eu era um estagiário e a IA um analista sênior, pedindo um "Code Review".
- A IA avaliou o script e apontou "code smells" (cheiros de mau código), explicando de forma muito didática o porquê certas lógicas — como aninhamentos profundos (*código Hadouken*) — são ruins.
- Aprendi os conceitos de *Type Hints* para validação em IDEs e de *Early Return* para tratar caminhos de erro no começo da função sem precisar "enclausurar" o caminho de sucesso dentro de um `else`.
