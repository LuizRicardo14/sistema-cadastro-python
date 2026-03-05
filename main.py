usuarios = []

while True:
    print("\n=== SISTEMA DE CADASTRO ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        
        usuario = {
            "nome": nome,
            "idade": idade
        }

        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            print("\n=== LISTA DE USUÁRIOS ===")
            for u in usuarios:
                print("Nome:", u["nome"], "| Idade:", u["idade"])

    elif opcao == "3":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")