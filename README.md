# Atividade Formativa


## Como o programa funciona

O programa é um gestor de portfólio de projetos via linha de comando (`gestor.py`). Ele opera em um loop contínuo (infinito) que interage com o usuário até que o comando de saída seja acionado.

### Passo a passo e variáveis utilizadas:

1. **Início do Loop (`while True`)**: O programa começa a rodar e fica aguardando instruções indefinidamente.
2. **Entrada do Usuário**: A variável `comando` recebe o texto que o usuário digita. Esse texto é convertido para letras maiúsculas para facilitar a verificação das opções, que são `ABOUT`, `ADD` e `QUIT`.
3. **Verificação do comando**:
   - Se a variável `comando` for igual a `"ABOUT"`: Imprime na tela o título do sistema ("Gestor de Portfólio do Gabriel").
   - Se a variável `comando` começar com `"ADD"`:
     - O programa pergunta quantos projetos o usuário quer adicionar e tenta converter esse valor para um número inteiro, salvando na variável `quantidade`.
     - Caso o usuário digite um texto inválido no lugar do número, o bloco `try/except` captura o erro e avisa o usuário.
     - Caso o número na variável `quantidade` seja menor ou igual a zero, exibe uma mensagem de erro ("O número de projetos deve ser maior que zero").
     - Se a `quantidade` for um número válido e positivo, inicia-se uma estrutura de repetição (`for`) que roda o número exato de vezes solicitado.
     - A cada iteração desse loop, o nome do projeto é solicitado e armazenado na variável `nome_projeto`, exibindo em seguida uma mensagem de sucesso na tela.
   - Se a variável `comando` for igual a `"QUIT"`: Imprime uma mensagem alertando que está saindo e aciona a palavra-chave `break`, que interrompe o loop principal (`while True`).
   - Se a variável `comando` não corresponder a nenhuma das opções acima, exibe uma mensagem de erro avisando que o comando não foi reconhecido.
4. **Encerramento**: Assim que o loop é interrompido, o programa finaliza exibindo a mensagem `"Hasta la vista!"`.
