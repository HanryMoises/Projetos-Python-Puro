carrinho = []

ctl = True


def menu():
    while ctl == True:
        opt = input(
            "Selecione uma opção\n\n"
            "[1]adicionar produto"
            "\n[2]listar produtos"
            "\n[3]atualizar produto"
            "\n[4]limpar carrinho"
            "\n[5]remover produto"
            "\n\nOpção: ")
        match opt:
            case '2':
                listar()
            case '1':
                adicionar()
            case '3':
                atualizar()
            case '4':
                limpar()
            case '5':
                remover()
            case '0':
                print("Volte sempre")
                break


def remover():
    n = input("código do item? ")
    for p in carrinho:
        if p[0] == n:
          del p[1]
          del p[1]
        elif p[0] != p:
            continue
    return


def atualizar():
    n = input("Código do item? ")
    for p in carrinho:
        if p[0] == n:
            p.append(input("Novo nome item:"))
            p.append(input("Novo valor item:"))
        elif p[0] != p:
            continue
    return


def listar():
    if len(carrinho) == 0:
        print("Sem produtos")
    else:
        print(carrinho)
    return


def adicionar():
    produto = []

    produto.append(input("código item:"))
    produto.append(input("Nome item:"))
    produto.append(input("valor item:"))
    carrinho.append(produto)


def limpar():
    carrinho.clear()
    print("carrinho removido")
    return


menu()
