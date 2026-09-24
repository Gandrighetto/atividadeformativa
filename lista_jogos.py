from datetime import datetime

def encontrar_jogo(jogos: list[dict], nome_jogo: str) -> dict | None:
    """Busca um jogo pelo nome na memória e o retorna. Retorna None se não achar."""
    for jogo in jogos:
        if jogo['nome'].lower() == nome_jogo.lower():
            return jogo
    return None

def mostrar_about() -> None:
    """Exibe as informações sobre o sistema."""
    print("Biblioteca de Jogos do Gabriel")

def adicionar_jogos(jogos: list[dict]) -> None:
    """Solicita a quantidade de jogos e adiciona novos dicionários de jogos à lista."""
    try:
        quantidade = int(input("Quantos jogos gostaria de cadastrar? "))
    except ValueError:
        print("ERRO: Por favor, digite um número válido.")
        return

    if quantidade <= 0:
        print("ERRO: O número de jogos deve ser maior que zero.")
        return

    for _ in range(quantidade):
        nome_jogo = input("Digite o nome do jogo: ").strip()
        if not nome_jogo:
            print("ERRO: O nome não pode estar vazio!")
            continue
            
        plataforma = input("Digite a plataforma do jogo: ").strip()
        novo_jogo = {
            "nome": nome_jogo,
            "concluido": False,
            "historico": [],
            "plataforma": plataforma if plataforma else "Desconhecida"
        }
        jogos.append(novo_jogo)
        print(f"SUCESSO: Jogo '{nome_jogo}' adicionado")

def listar_jogos(jogos: list[dict]) -> None:
    """Percorre a lista de jogos e imprime seus detalhes. Avisa se estiver vazia."""
    if not jogos:
        print("Não há nenhum jogo a ser listado no momento.")
        return
        
    for i, jogo in enumerate(jogos, start=1):
        status = "Concluído" if jogo["concluido"] else "Não concluído"
        print(f"{i}. Nome: {jogo['nome']} | Plataforma: {jogo['plataforma']} | Status: {status}")

def atualizar_jogo(jogos: list[dict]) -> None:
    """Busca um jogo e atualiza seus dados, registrando a mudança no histórico."""
    nome_editar = input("Digite o nome do jogo que deseja editar: ").strip()
    jogo = encontrar_jogo(jogos, nome_editar)
    
    if not jogo:
        print("ERRO: Jogo não encontrado.")
        return
        
    print(f"Editando: {jogo['nome']}")
    
    novo_nome = input(f"Novo nome (pressione Enter para manter '{jogo['nome']}'): ").strip()
    nova_plataforma = input(f"Nova plataforma (pressione Enter para manter '{jogo['plataforma']}'): ").strip()
    novo_status_input = input(f"Concluído? (s/n, pressione Enter para manter atual): ").strip().lower()
    
    # Atualiza dados
    if novo_nome:
        jogo['nome'] = novo_nome
    if nova_plataforma:
        jogo['plataforma'] = nova_plataforma
    if novo_status_input == 's':
        jogo['concluido'] = True
    elif novo_status_input == 'n':
        jogo['concluido'] = False
        
    # Registra histórico
    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    jogo['historico'].append((data_atual, jogo['concluido'], jogo['nome']))
    
    print("SUCESSO: Jogo atualizado!")

def remover_jogo(jogos: list[dict]) -> None:
    """Busca um jogo pelo nome e o remove da lista, se existir."""
    nome_remover = input("Digite o nome do jogo que deseja remover: ").strip()
    jogo = encontrar_jogo(jogos, nome_remover)
    
    if not jogo:
        print("ERRO: Jogo não encontrado.")
        return
        
    jogos.remove(jogo)
    print(f"SUCESSO: Jogo '{jogo['nome']}' removido.")

def biblioteca() -> None:
    """Função principal que gerencia o loop do programa e o menu de comandos."""
    jogos = []
    while True:
        comando = input("Digite um comando (ABOUT/ADD/LIST/UPDATE/DELETE/QUIT): ").upper()
        
        match comando:
            case "ABOUT":
                mostrar_about()
            case "ADD":
                adicionar_jogos(jogos)
            case "LIST":
                listar_jogos(jogos)
            case "UPDATE":
                atualizar_jogo(jogos)
            case "DELETE":
                remover_jogo(jogos)
            case "QUIT":
                print("Saindo da Biblioteca de Jogos")
                break
            case _:
                print("ERRO: Comando não reconhecido.")
                
    print("Hasta la vista!")

if __name__ == "__main__":
    biblioteca()
