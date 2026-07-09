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
    item = input("Qual item deseja registrar?")
    while True:
            if item not in estoque:
                print("Item ainda nao cadastrado!")
                choice = input("Quer cadastrar? [S/N] ")
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
                choice = input("Quer continuar registrando ? [S/N] ")
                if choice == "S":
                    registrar_item()
                else:
                    print("Ok, retornando ao menu principal...")
                break


def listar_estoque():
    for item, quantidade in estoque.items():
        print(f"{item}: {quantidade}")

item = input("Qual item deseja cadastrar?")
cadastrar_item(item)
registrar_item()
listar_estoque()