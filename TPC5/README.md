# TPC5: MÁQUINA DE VENDAS
#### Autor: José Afonso Lopes Correia, A100610  

## Resumo:
Programa em Python que simula o funcionamento de uma máquina de vendas. Este programa permite que os utilizadores interajam com a máquina inserindo comandos para listar produtos, adicionar moedas, selecionar produtos e sair do mesmo.

Para tal, o programa utiliza um analisador léxico para interpretação dos diversos comandos:

`listar` - lista os produtos disponíveis

`moeda <lista de moedas>` - adiciona a quantia total inserida ao saldo

`selecionar <id produto>` - prodeece à compra do produto selecionado, caso o saldo seja suficiente

`sair` - calcula o troco e termina o programa

### Manipulação de Dados dos Produtos:
Os dados dos produtos são fornecidos a partir de um ficheiro JSON, seguindo uma estrutura específica que inclui o ID do produto, o nome e o preço.

## Demonstração:
```
Bem-vindo à máquina de vendas do Zé!
         ____________________________________________
        |############################################|
        |#|                           |##############|
        |#|  =====  ..--''`  |~~``|   |##|````````|##|
        |#|  |   |  \     |  :    |   |##| Exact  |##|
        |#|  |___|   /___ |  | ___|   |##| Change |##|
        |#|  /=__\\  ./.__\\   |/,__\\|##| Only   |##|
        |#|  \\__//   \\__//    \\__//|##|________|##|
        |#|===========================|##############|
        |#|```````````````````````````|##############|
        |#| =.._      +++     //////  |##############|
        |#| \\/  \\     | |     \\    |#|`````````|##|
        |#|  \\___\\    |_|     /___ /|#| _______ |##|
        |#|  / __\\\\  /|_|\\   // __\|#| |1|2|3| |##|
        |#|  \\__//-  \\|_//   -\\__//|#| |4|5|6| |##|
        |#|===========================|#| |7|8|9| |##|
        |#|```````````````````````````|#| ``````` |##|
        |#| ..--    ______   .--._.   |#|[=======]|##|
        |#| \\   \\   |    |   |    | |#|  _   _  |##|
        |#|  \\___\\  : ___:   | ___| |#| ||| ( ) |##|
        |#|  / __\\  |/ __\\   // __\\|#| |||  `  |##|
        |#|  \\__//   \\__//  /_\\__//|#|  ~      |##|
        |#|===========================|#|_________|##|
        |#|```````````````````````````|##############|
        |############################################|
        |#|||||||||||||||||||||||||||||####```````###|
        |#||||||||||||PUSH|||||||||||||####\\|||||/##|
        |############################################|
        \\\\\\\\\\\\\\\\\\\\\\///////////////////////
         |_________________________________|CR8|___|

Comandos disponíveis: listar, moeda, selecionar, sair

$ listar
    Número      |            Nome                        |      Preço      |   Quantidade
       1        |        Par de meias                    |       1.8       |       4
       2        |        Cheirinho para o carro          |       1.95      |       3
       3        |        Guarda-Chuva                    |       3.5       |       5
       4        |        Gomas dos Ursinhos              |       1.65      |       4
       5        |        Bolacha-Joao                    |       0.45      |       6
       6        |        Palmier de Chocolate            |       0.75      |       6
       7        |        Agua                            |       0.6       |       8
       8        |        Cola-Cola                       |       0.95      |       8
       9        |        Hyper Bock Mini                 |       1.2       |       1

$ moeda 2e, 50c, 1e, 10c
Saldo: 3.6€

$ selecionar 9
Produto Hyper Bock Mini comprado. Saldo restante: 2.4€

$ selecionar 9
Produto Hyper Bock Mini esgotado.

$ sair
Troco:
1 x 2€
0 x 1€
0 x 0.5€
2 x 0.2€
0 x 0.1€
0 x 0.05€
Obrigado por usar a máquina de vendas do Zé!
```

Recorreu-se à biblioteca [ply](https://www.dabeaz.com/ply/ply.html), uma ferramenta para a construção de analisadores léxicos e sintáticos.