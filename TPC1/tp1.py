class TP1():
    listEscalao = []
    listModalidades = []
    listAptos = []
    listInaptos = []
    listIdades = []


    #Função que lê a informação do ficheiro para um modelo, previamente pensado em memória
    def saveInfo(self, arrayInfo):
        with open('emd.csv', 'r') as f_in, open('emd.txt', 'w') as f_out:
                content = f_in.read()
                f_out.write(content)
        # criar um ficheiro txt com os mesmos campos do csv
        # guardar os dados num array de arrays, em que cada linha é um array
        with open('emd.txt', 'r+') as fp: 
                lines = fp.readlines() 
                fp.seek(0)
                fp.truncate()
                fp.writelines(lines[1:])
        for line in lines: 
                #print (line)
                x = line.split(",") #separa os valores entre as virgulas
                arrayInfo.append(x)
        #print(arrayInfo) 
                
    #Função que ordena alfabeticamente as modalidades desportivas
    def ordModalidades(self, arrayInfo):
        for i in range(len(arrayInfo)):
            if arrayInfo[i][8] not in self.listModalidades:
                self.listModalidades.append(arrayInfo[i][8])
        self.listModalidades.sort()
        print("Lista de modalidades ordenada alfabeticamente: ", self.listModalidades)
        return self.listModalidades
    
    #Função que calcula a percentagem de atletas aptos e inaptos para a prática desportiva
    def calcAtletasAptos(self, arrayInfo):
        aptos=0
        inaptos=0
        for i in range(len(arrayInfo)):
            if arrayInfo[i][12].strip() == 'true':
                aptos+=1
            if arrayInfo[i][12].strip()== 'false':
                inaptos+=1
        total = aptos+inaptos
        percAptos = (aptos/total)*100
        percInaptos = (inaptos/total)*100
        print("Percentagem de atletas aptos: ", percAptos, "%")
        print("Percentagem de atletas inaptos: ", percInaptos, "%")
        return percAptos, percInaptos
    
    #Função que calcula a distribuição de atletas por escalão etário (escalão = intervalo de 5 anos).
    def distrEscalaoAUX(self):
            #cria array entre 0 (idade minima) e 100 (idade máxima)
            lista = list(range(20,60))
            for i in range(0, len(lista),5):
               yield lista[i:i + 5]
    
    def distrEscalao(self, arrayInfo):
        listinha = list(self.distrEscalaoAUX())
        #print(listinha)
        for a in listinha:
            a.append(0) #adiciono um inteiro no fim de cada array para contabilizar o número de atletas desse array(escalão)
        for a in listinha:
            for line in arrayInfo:
                for elem in a:
                    if str(elem).isdigit() and line[5].isdigit():
                        x= int(elem)
                        if int(line[5]) == x:
                            newValue = a[-1] + 1
                            a[-1] = newValue  # increment the value of the last element of the array

                    #print(listinha)
        for a in listinha:
            if len(a)==6:
                NRmin = a[0]
                NRmax= a[4]
                NRatletas = a[5]
                print ("No escalão [",NRmin,",",NRmax,"] existem ", NRatletas,"altletas.")
                triplinho =(NRmin,NRmax,NRatletas)
                self.listEscalao.append(triplinho)
         
