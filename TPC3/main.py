import re
import sys

def onoff(file):
    listaux = []
    sum = 0
    switch = False
    for line in file:
        capture = re.findall(r'(on|off|=|[\+\-]?\d+)', line, re.IGNORECASE)
        listaux.append(capture)
    lista = [item for sublist in listaux for item in sublist]
    for i in lista:
        if i.lower() == "on":
            switch = True
        elif i.lower() == "off":
            switch = False
        elif i.isdigit() and switch:
            sum += int(i)
        elif i[0] == "+" and switch:
            sum += int(i[1:])
        elif i[0] == "-" and switch:
            sum -= int(i[1:])
        elif i.lower() == "=":
            print("Somatório = ", sum)
            

def main(args):
    #get file name from command line´
    if len(args) < 2:
        return
    
    with open(args[1], 'r') as file:
        onoff(file)

if __name__ == "__main__":
    main(args=sys.argv)