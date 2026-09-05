def biblioteca():
    jogos = []
    while True:
        comando = input("Digite um comando (ABOUT/ADD/LIST/QUIT): ").upper()
        
        if comando == "ABOUT":
            print("Biblioteca de Jogos do Gabriel")
        elif comando == "ADD":
            try:
                quantidade = int(input("Quantos jogos gostaria de cadastrar? "))
                if quantidade <= 0:
                    print("ERRO: O número de jogos deve ser maior que zero.")
                else:
                    for _ in range(quantidade):
                        nome_jogo = input("Digite o nome do jogo: ").strip()
                        if nome_jogo:
                            jogos.append(nome_jogo)
                            print(f"SUCESSO: Jogo '{nome_jogo}' adicionado")
                        else:
                            print("ERRO: O nome não pode estar vazio!")
            except ValueError:
                print("ERRO: Por favor, digite um número válido.")
        elif comando == "LIST":
            if not jogos:
                print("Não há nenhum jogo a ser listado no momento.")
            else:
                for i, jogo in enumerate(jogos, start=1):
                    print(f"{i}. {jogo}")
        elif comando == "QUIT":
            print("Saindo da Biblioteca de Jogos")
            break
        else:
            print("ERRO: Comando não reconhecido.")
    print("Hasta la vista!")

if __name__ == "__main__":
    biblioteca()
