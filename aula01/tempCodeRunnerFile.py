while True:
    print("Menu:")
    print("1 - Olá Mundo")
    print("2 - Bom dia")
    print("3 - Boa noite")
    print("0 - Sair")

    escolha = int(input("Escolha uma opção: "))

    match escolha : 
        case 1:
            print("Olá Mundo")
        case 2:
            print("Bom dia")
        case 3:
            print("Boa noite")
        case 0:
            print("Saindo do programa.")
            break
        case default:
            print("Opção inválida")