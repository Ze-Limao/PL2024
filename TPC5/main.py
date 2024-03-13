import sys
import json
import ply.lex as lex

#Máquina de vendas
tokens = (
    "LISTAR",
    "MOEDA",
    "SELECIONAR",
    "SAIR"
)

def t_LISTAR(t):
    r'listar'
    return t

def t_MOEDA(t):
    r'moeda[ ]([5c|10c|20c|50c|1e|2e],?)+' # Uma ou mais moedas separadas por vírgula
    return t

def t_SELECIONAR(t):
    r'selecionar[ ]\d+'
    return t

def t_SAIR(t):
    r'sair'
    return t


t_ignore = '\t\n'

def t_error(t):
    sys.stderr.write(f"Error: Unexpected command {t.value[0]}\n")
    t.lexer.skip(1) # Ignorar o token

def get_change(saldo):
    change = {}
    coins = [2, 1, 0.5, 0.2, 0.1, 0.05]
    for coin in coins:
        change[coin] = int(saldo // coin)
        saldo = round(saldo % coin, 2)
    return change


def main(argv):
    if (len(argv) < 2):
        print("Usage: python main.py <input_file>")
        return

    # Ler o ficheiro json
    with open(argv[1], "r") as file:
        data = json.load(file)

    # Criar a tabela de produtos
    produtos = data["produtos"]
    tabela = {}
    for produto in produtos:
        tabela[produto["id"]] = produto
    

    lexer = lex.lex() # Criar o lexer
    saldo = 0 # Saldo do utilizador
    print("""
Bem-vindo à máquina de vendas do Zé!
         ____________________________________________
        |############################################|
        |#|                           |##############|
        |#|  =====  ..--''`  |~~``|   |##|````````|##|
        |#|  |   |  \     |  :    |   |##| Exact  |##|
        |#|  |___|   /___ |  | ___|   |##| Change |##|
        |#|  /=__\\  ./.__\\   |/,__\\   |##| Only   |##|
        |#|  \\__//   \\__//    \\__//   |##|________|##|
        |#|===========================|##############|
        |#|```````````````````````````|##############|
        |#| =.._      +++     //////  |##############|
        |#| \\/  \\     | |     \\    \\  |#|`````````|##|
        |#|  \\___\\    |_|     /___ /  |#| _______ |##|
        |#|  / __\\\\  /|_|\\   // __\\   |#| |1|2|3| |##|
        |#|  \\__//-  \\|_//   -\\__//   |#| |4|5|6| |##|
        |#|===========================|#| |7|8|9| |##|
        |#|```````````````````````````|#| ``````` |##|
        |#| ..--    ______   .--._.   |#|[=======]|##|
        |#| \\   \\   |    |   |    |   |#|  _   _  |##|
        |#|  \\___\\  : ___:   | ___|   |#| ||| ( ) |##|
        |#|  / __\\  |/ __\\   // __\\   |#| |||  `  |##|
        |#|  \\__//   \\__//  /_\\__//   |#|  ~      |##|
        |#|===========================|#|_________|##|
        |#|```````````````````````````|##############|
        |############################################|
        |#|||||||||||||||||||||||||||||####```````###|
        |#||||||||||||PUSH|||||||||||||####\\|||||/###|
        |############################################|
        \\\\\\\\\\\\\\\\\\\\\\///////////////////////
         |________________________________| CR8|___|
""")
    print("Comandos disponíveis: listar, moeda, selecionar, sair")
    for line in sys.stdin: # Para cada linha do input
        lexer.input(line)
        for token in lexer:
            if token.type == "LISTAR":
                print('     Número     |            Nome                        |       Preço       |    Quantidade    ')
                for produto in produtos:
                    print(f'       {produto["id"]}        |        {produto["nome"]: <24}        |       {produto["preco"]: <5}       |         {produto["quantidade"]}    ')

            elif token.type == "MOEDA":
                moedas = token.value.split(" ")[1].split(",")
                for moeda in moedas:
                    if moeda[-1] == "e": # moeda[-1] para remover o "e"
                        saldo += float(moeda[:-1])
                    else: 
                        saldo += float(moeda[:-1]) / 100 # Se for uma moeda de cêntimos
                print(f"Saldo: {saldo}€")
            
            elif token.type == "SELECIONAR":
                id = int(token.value.split(" ")[1])
                if id in tabela:
                    produto = tabela[id]
                    if produto["quantidade"] == 0:
                        print(f"Produto {produto['nome']} esgotado.")
                    elif saldo >= produto["preco"] and produto["quantidade"] > 0:
                        saldo -= produto["preco"]
                        produto["quantidade"] -= 1
                        print(f"Produto {produto['nome']} comprado. Saldo restante: {saldo}€")
                    else:
                        print("Saldo insuficiente")
                else:
                    print(f"Produto com id {id} não existe")

            elif token.type == "SAIR":
                change = get_change(saldo)
                # Imprimir o troco com asccii art
                print("Troco:")
                for coin in change:
                    print(f"{change[coin]} x {coin}€")
                print("Obrigado por usar a máquina de vendas do Zé!")
                return


if __name__ == "__main__":
    main(sys.argv)