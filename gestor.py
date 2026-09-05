def gestor():
    while True:
        comando = input("Digite um comando (ABOUT/ADD/QUIT): ").upper()
        
        if comando == "ABOUT":
            print("Gestor de Portfólio do Gabriel")
        elif comando.startswith("ADD"):
            try:
                quantidade = int(input("Quantos projetos gostaria de cadastrar? "))
                if quantidade <= 0:
                    print("ERRO: O número de projetos deve ser maior que zero.")
                else:
                    for _ in range(quantidade):
                        nome_projeto = input("Digite o nome do projeto: ")
                        print(f"SUCESSO: Projeto '{nome_projeto}' adicionado")
            except ValueError:
                print("ERRO: Por favor, digite um número válido.")
        elif comando == "QUIT":
            print("Saindo do Gestor de Portfólio")
            break
        else:
            print("ERRO: Comando não reconhecido.")
    print("Hasta la vista!")

if __name__ == "__main__":
    gestor()
