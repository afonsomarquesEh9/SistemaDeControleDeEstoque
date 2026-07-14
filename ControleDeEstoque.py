import datetime

# Cadastro de ítens no estoque

estoque = {}
movimentacoes = []

def cadastrar_item(item):
    if item not in estoque:
        estoque[item] = 0
        datetime.datetime.now()
        movimentacoes.append({"Tipo":"Cadastro","Data":datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
        print("Item cadastrado com sucesso!")
    else:
        print("Item já cadastrado!")
        return

# Registro de ítens no estoque

def registrar_item():
    item = input("Digite o item a ser registrado ou 'SAIR' para sair: ")
    if item == "SAIR":
        return
    while True:
            if item not in estoque:
                print("Item ainda nao cadastrado!")
                choice = input("Deseja cadastrar? [S/N] ").upper()
                if choice == "S":
                    cadastrar_item(item)
                    continue
                elif choice == "N":
                    print("Ok, retornando ao menu principal...")
                    break

            else:
                quantity = int(input("Quantos ítens registrar? "))
                estoque[item] += quantity
                movimentacoes.append({"Tipo": "Registro", "Data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
                print("Ítens registrados com sucesso!")
                choice = input("Deseja continuar registrando ? [S/N] ").upper()
                if choice == "S":
                    registrar_item()
                else:
                    print("Ok, retornando ao menu principal...")
                break

# Registro de saída de produtos do estoque

def registrar_saida():
    item = input("Digite o nome do item que deseja registrar saída ou 'SAIR' para sair: ").upper()
    if item == "SAIR":
        return
    while True:
        if item not in estoque:
            print("Item nao cadastrado!")
            choice = input("Deseja cadastrar? [S/N] ").upper()
            if choice == "S":
                cadastrar_item(item)
                continue
            elif choice == "N":
                print("Ok, retornando ao menu principal...")
                break

        else:
            quantity = int(input("Quantos ítens deseja registrar saída? "))
            estoque[item] -= quantity
            movimentacoes.append({"Tipo": "Saída", "Data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
            print("Saída de ítens registrada com sucesso!")
            choice = input("Deseja continuar registrando saída de ítens ? [S/N] ").upper()
            if choice == "S":
                registrar_item()
            else:
                print("Ok, retornando ao menu principal...")
            break

def listar_movimentacoes():
    for mov in movimentacoes:
        print(mov)


def listar_estoque():
    for item_estoque, quantidade in estoque.items():
        print(f"{item_estoque}: {quantidade}")

item = input("Qual item deseja cadastrar?")
cadastrar_item(item)
registrar_item()
listar_estoque()
listar_movimentacoes()