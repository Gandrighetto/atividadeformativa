# Atividade Formativa


## Como o programa funciona

O programa é uma biblioteca de jogos via linha de comando (`lista_jogos.py`). Ele opera em um loop contínuo (infinito) que interage com o usuário até que o comando de saída seja acionado. O sistema possui uma "memória" temporária (a variável de lista `jogos`) que guarda as informações durante a execução.

### Passo a passo e variáveis utilizadas:

1. **Memória do Sistema**: Antes de iniciar o loop, uma lista vazia chamada `jogos` é criada. Ela é a responsável por armazenar todos os jogos adicionados. Agora, cada jogo é representado por um **dicionário** contendo as chaves: `nome` (texto), `plataforma` (texto), `concluido` (booleano) e `historico` (uma lista de tuplas de log).
2. **Início do Loop (`while True`)**: O programa começa a rodar e fica aguardando instruções indefinidamente.
3. **Entrada do Usuário**: A variável `comando` recebe o texto que o usuário digita. Esse texto é convertido para letras maiúsculas para facilitar a verificação das opções, que agora são `ABOUT`, `ADD`, `LIST`, `UPDATE`, `DELETE` e `QUIT`.
4. **Verificação do comando**:
   - Se a variável `comando` for igual a `"ABOUT"`: Imprime na tela o título do sistema.
   - Se a variável `comando` for igual a `"ADD"`:
     - O programa pergunta quantos jogos o usuário quer adicionar.
     - Inicia-se uma estrutura de repetição (`for`) que roda a quantidade de vezes solicitada.
     - Para cada item, o programa pede o nome e a plataforma do jogo. Com essas informações, ele monta um dicionário (o status `concluido` inicia como `False` por padrão e o `historico` inicia vazio) e o guarda na lista `jogos` através do método `.append()`.
   - Se a variável `comando` for igual a `"LIST"`:
     - Verifica se a lista `jogos` está vazia.
     - Se houver jogos, percorre a lista de dicionários usando `enumerate()` num loop `for`. Para cada dicionário de jogo, extrai e imprime de maneira formatada o seu nome, plataforma e status de conclusão.
   - Se a variável `comando` for igual a `"UPDATE"`:
     - Pergunta o nome do jogo que será editado e realiza uma busca iterando a lista com um loop `for`.
     - Caso o jogo seja encontrado (`jogo['nome']` for igual ao nome digitado), o sistema pede os novos valores para nome, plataforma e status.
     - Após atualizar as chaves no dicionário, captura a data e hora atual via biblioteca `datetime` e anexa uma **tupla** no formato `(data_atual, novo_status, novo_nome)` dentro da chave `historico` do respectivo jogo.
   - Se a variável `comando` for igual a `"DELETE"`:
     - Pergunta o nome do jogo a remover e procura iterando na lista.
     - Quando o jogo for encontrado, utiliza o método `.remove()` para deletar o dicionário completo da lista `jogos`.
   - Se a variável `comando` for igual a `"QUIT"`: Aciona a palavra-chave `break`, que interrompe o loop principal (`while True`) e finaliza a execução.
   - Comandos desconhecidos geram uma mensagem de erro avisando que o comando não foi reconhecido.
5. **Encerramento**: Assim que o loop é interrompido, o programa finaliza exibindo a mensagem `"Hasta la vista!"`.

## Estrutura do Código (Boas Práticas)

Nesta versão, a aplicação evoluiu de um script procedural simples para um código modular baseado em funções. Cada funcionalidade do menu (`adicionar_jogos`, `listar_jogos`, `atualizar_jogo`, `remover_jogo`) foi delegada à sua própria função.

Para garantir qualidade de nível profissional, o código conta com:
- **Type Hints**: Variáveis e retornos explicitamente tipados (ex: `jogos: list[dict]`), auxiliando analisadores estáticos de código.
- **Docstrings**: Pequenos blocos de texto (`"""`) detalhando o que cada função faz.
- **Early Returns (Retorno Antecipado)**: Estruturação das lógicas de forma que possíveis erros encerram a função nas primeiras linhas, reduzindo a complexidade ciclomática e dispensando a necessidade de blocos `else` gigantes.
- **Match / Case**: Utilização do recurso (introduzido no Python 3.10) para o roteamento do input do usuário, substituindo a pesada leitura visual que vários `elif` em sequência causam.
