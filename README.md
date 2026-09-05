# Atividade Formativa


## Como o programa funciona

O programa é uma biblioteca de jogos via linha de comando (`lista_jogos.py`). Ele opera em um loop contínuo (infinito) que interage com o usuário até que o comando de saída seja acionado. O sistema possui uma "memória" temporária (a variável de lista `jogos`) que guarda as informações durante a execução.

### Passo a passo e variáveis utilizadas:

1. **Memória do Sistema**: Antes de iniciar o loop, uma lista vazia chamada `jogos` é criada. Ela é a responsável por armazenar todos os nomes de jogos adicionados.
2. **Início do Loop (`while True`)**: O programa começa a rodar e fica aguardando instruções indefinidamente.
3. **Entrada do Usuário**: A variável `comando` recebe o texto que o usuário digita. Esse texto é convertido para letras maiúsculas para facilitar a verificação das opções, que são `ABOUT`, `ADD`, `LIST` e `QUIT`.
4. **Verificação do comando**:
   - Se a variável `comando` for igual a `"ABOUT"`: Imprime na tela o título do sistema ("Biblioteca de Jogos do Gabriel").
   - Se a variável `comando` for igual a `"ADD"`:
     - O programa pergunta quantos jogos o usuário quer adicionar e tenta converter esse valor para um número inteiro, salvando na variável `quantidade`.
     - Caso o usuário digite um texto inválido no lugar do número, o bloco `try/except` captura o erro e avisa o usuário.
     - Caso o número na variável `quantidade` seja menor ou igual a zero, exibe uma mensagem de erro ("O número de jogos deve ser maior que zero").
     - Se a `quantidade` for um número válido e positivo, inicia-se uma estrutura de repetição (`for`) que roda o número exato de vezes solicitado.
     - A cada iteração desse loop, o nome do jogo é solicitado e a entrada é limpa de espaços vazios (usando `.strip()`).
     - O programa verifica se o nome não ficou vazio. Se for válido, é guardado na lista `jogos` através do método `.append()`, e é exibida uma mensagem de sucesso. Caso o nome seja vazio, um erro é exibido.
   - Se a variável `comando` for igual a `"LIST"`:
     - O programa verifica se a lista `jogos` está vazia usando uma checagem simples (`not jogos`). Se estiver, exibe um aviso.
     - Se houver jogos na lista, ele usa a função `enumerate()` em um loop `for` para percorrer a memória e imprimir cada jogo já enumerado na tela (exemplo: "1. Jogo X").
   - Se a variável `comando` for igual a `"QUIT"`: Imprime uma mensagem alertando que está saindo e aciona a palavra-chave `break`, que interrompe o loop principal (`while True`).
   - Se a variável `comando` não corresponder a nenhuma das opções acima, exibe uma mensagem de erro avisando que o comando não foi reconhecido.
5. **Encerramento**: Assim que o loop é interrompido, o programa finaliza exibindo a mensagem `"Hasta la vista!"`.
