from tp1 import TP1

def main():
    res = TP1()
    c=-1  
    while c!=0:
        print("***** RESOLUÇÃO DO TPC1 *****")
        print("  ")
        print("1 -> Calcula a lista ordenada alfabeticamente das modalidades desportivas")
        print("2 -> Calcula a percentagens de atletas aptos e inaptos para a prática desportiva")
        print("3 -> Calcula a distribuição de atletas por escalão etário (escalão = intervalo de 5 anos).")
        print("0 -> Sair")
        print("******************************")
        c = int(input("Indique a opção pretendida-> "))
        print (" ")
        arrayInfo = []
        if c==1:
            res.saveInfo(arrayInfo)
            res.ordModalidades(arrayInfo)
            print (" ")
        if c==2:
            res.saveInfo(arrayInfo)
            res.calcAtletasAptos(arrayInfo)
            print (" ")
        if c==3:
            res.saveInfo(arrayInfo)
            res.distrEscalao(arrayInfo)
            print (" ")


if __name__ == "__main__":
    main()