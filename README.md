# Atividade Formativa


## Como o programa funciona

O programa é uma biblioteca de jogos via linha de comando (`lista_jogos.py`). Ele opera em um loop contínuo (infinito) que interage com o usuário até que o comando de saída seja acionado. O sistema possui uma "memória" temporária (a variável de lista `jogos`) que guarda as informações durante a execução.

### Passo a passo e variáveis utilizadas:

1. **Memória do Sistema**: Antes de iniciar o loop, uma lista vazia chamada `jogos` é criada. Ela é a responsável por armazenar todos os nomes de jogos adicionados.
2. **Início do Loop (`while True`)**: O programa começa a rodar e fica aguardando instruções indefinidamente.
3. **Entrada do Usuário**: A variável `comando` recebe o texto que o usuário digita. Esse texto é convertido para letras maiúsculas para facilitar a verificação das opções, que são `ABOUT`, `ADD`, `LIST` e `QUIT`.
4. **Verificação do comando**:
   - Se a variável `comando` for igual a `"ABOUT"`: Imprime na tela o título do sistema ("Biblioteca de Jogos do Gabriel").
   - Se a variável `comando` começar com `"ADD"`:
     - O programa pergunta quantos jogos o usuário quer adicionar e tenta converter esse valor para um número inteiro, salvando na variável `quantidade`.
     - Caso o usuário digite um texto inválido no lugar do número, o bloco `try/except` captura o erro e avisa o usuário.
     - Caso o número na variável `quantidade` seja menor ou igual a zero, exibe uma mensagem de erro ("O número de jogos deve ser maior que zero").
     - Se a `quantidade` for um número válido e positivo, inicia-se uma estrutura de repetição (`for`) que roda o número exato de vezes solicitado.
     - A cada iteração desse loop, o nome do jogo é solicitado e armazenado na variável `nome_jogo`.
     - O nome recebido é guardado dentro da memória adicionando-o à lista `jogos` através do método `.append()`. Por fim, é exibida uma mensagem de sucesso na tela.
   - Se a variável `comando` for igual a `"LIST"`:
     - O programa verifica o tamanho da memória. Se a lista `jogos` estiver vazia (tamanho 0), exibe um aviso informando que não há jogos no momento.
     - Se houver jogos na lista, ele usa um loop `for` e uma variável contadora `i` para percorrer a memória e imprimir cada jogo enumerado na tela (exemplo: "1. Jogo X").
   - Se a variável `comando` for igual a `"QUIT"`: Imprime uma mensagem alertando que está saindo e aciona a palavra-chave `break`, que interrompe o loop principal (`while True`).
   - Se a variável `comando` não corresponder a nenhuma das opções acima, exibe uma mensagem de erro avisando que o comando não foi reconhecido.
5. **Encerramento**: Assim que o loop é interrompido, o programa finaliza exibindo a mensagem `"Hasta la vista!"`.
