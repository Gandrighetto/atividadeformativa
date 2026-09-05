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
