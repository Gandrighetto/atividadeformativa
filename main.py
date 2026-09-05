def main():
    comando = input("Digite um comando (ABOUT/QUIT): ").upper()
    
    if comando == "ABOUT":
        print("Gestor de Portfólio do Gabriel")
    elif comando == "QUIT":
        print("Saindo do Gestor de Portfólio")
    else:
        print("ERRO: Comando não reconhecido.")
    print("Hasta la vista!")

if __name__ == "__main__":
    main()
