# clinica_vida.py
def menu():
    print("=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")

def cadastrar(pacientes):
    nome = input("Nome do paciente: ").strip()
    idade = int(input("Idade: "))
    telefone = input("Telefone: ").strip()
    pacientes.append({"nome": nome, "idade": idade, "telefone": telefone})
    print("Paciente cadastrado com sucesso!")

def estatisticas(pacientes):
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    total = len(pacientes)
    media = sum(p['idade'] for p in pacientes) / total
    mais_novo = min(pacientes, key=lambda p: p['idade'])
    mais_velho = max(pacientes, key=lambda p: p['idade'])
    print(f"Total: {total}, Idade média: {media:.2f}")
    print(f"Mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

def buscar(pacientes):
    nome = input("Nome a buscar: ").strip().lower()
    resultados = [p for p in pacientes if nome in p['nome'].lower()]
    for p in resultados:
        print(p)
    if not resultados:
        print("Paciente não encontrado.")

def main():
    pacientes = []
    while True:
        menu()
        op = input("Escolha uma opção: ").strip()
        if op == "1":
            cadastrar(pacientes)
        elif op == "2":
            estatisticas(pacientes)
        elif op == "3":
            buscar(pacientes)
        elif op == "4":
            for p in pacientes:
                print(p)
        elif op == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
