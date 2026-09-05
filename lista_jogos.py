def biblioteca():
    jogos = []
    while True:
        comando = input("Digite um comando (ABOUT/ADD/LIST/QUIT): ").upper()
        
        if comando == "ABOUT":
            print("Biblioteca de Jogos do Gabriel")
        elif comando.startswith("ADD"):
            try:
                quantidade = int(input("Quantos jogos gostaria de cadastrar? "))
                if quantidade <= 0:
                    print("ERRO: O número de jogos deve ser maior que zero.")
                else:
                    for _ in range(quantidade):
                        nome_jogo = input("Digite o nome do jogo: ")
                        jogos.append(nome_jogo)
                        print(f"SUCESSO: Jogo '{nome_jogo}' adicionado")
            except ValueError:
                print("ERRO: Por favor, digite um número válido.")
        elif comando == "LIST":
            if len(jogos) == 0:
                print("Não há nenhum jogo a ser listado no momento.")
            else:
                for i in range(len(jogos)):
                    print(f"{i + 1}. {jogos[i]}")
        elif comando == "QUIT":
            print("Saindo da Biblioteca de Jogos")
            break
        else:
            print("ERRO: Comando não reconhecido.")
    print("Hasta la vista!")

if __name__ == "__main__":
    biblioteca()
