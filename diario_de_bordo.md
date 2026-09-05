# Diário de Bordo

Este documento serve como um registro do desenvolvimento do projeto **Biblioteca de Jogos**.

## 04 de Setembro de 2026

**O que foi feito:**
- Configuração inicial do repositório Git e solução de problemas de autenticação (email e nome).
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
  - Implementação da validação "Pythonica" de lista vazia (`if not jogos:`).
  - Melhoria na legibilidade do loop `LIST` utilizando a função nativa `enumerate()`.

**Próximos passos:**

