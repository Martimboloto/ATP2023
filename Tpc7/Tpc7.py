import numpy as np
import matplotlib.pyplot as plt

def LoadPolinomials(file):
    polinomials = list()
    with open(file, "r") as file:
        for i in file:
            polinomials.extend(i.split("|"))
    return polinomials


def dividePolinomial(polinomial):
    splited = polinomial.split(" ")
    for j in range (len(splited)):
        if splited[j] == "-" or splited[j] == "+":
            splited[j+1] = splited[j] + splited[j+1]

    for k in splited:
        if k == "+" or k == "-":
            splited.pop(splited.index(k))
    dividedpol = dict()
    for i in splited:
        if "^" in i:
            dividedpol[i.split("^"[0])] = i.split("^"[1])
        else:
            if "x" in i:
                dividedpol[i] = 1
            else:
                dividedpol[i] = 0
    return dividedpol

def calculatePolinomial(polinomial,x):
    dividedpol = dividePolinomial(polinomial)
    sum = 0
    for i in dividedpol.keys():
        if dividedpol[i] != 0:
            if i[:i.index("x")] == "": 
                sum = sum + (1*x)**int(dividedpol[i])
        else:
            sum = sum + float(i)

    return sum

def sumPolinomial(polinomial,polinomial1):
    dividedpol = dividePolinomial(polinomial)
    dividepol1 = dividePolinomial(polinomial1)
    newpol = dict()

    for i in dividedpol.keys():
        for j in dividepol1.keys():
            if(dividedpol[i] == dividepol1[j]):
                if (dividedpol != 0 and dividepol1[j] != 0):
                    if i[:i.index("x")] == "" and j[:j.index("x")] == "":
                        newpol["2"] = str(dividedpol[i])
                    elif i[:i.index("x")] == "" and j[:j.index("x")] != "":
                        newpol[str(1 + float(i[:i.index("X")]))] = str(dividedpol[i])
                    else:
                        newpol[str(float(i[:i.index("X")]) + float(j[:j.index("x")]))] = str(dividedpol[i])

                else:
                    newpol[str(float(i) + float(j))] = 0
    pol = ""
    for i in newpol.keys():
        if float(i) > 0:
            pol += "+" + str(i) + "x^" + str(newpol[i]) + " "
        else: 
            pol += str(i) + "x^" + str(newpol[i]) + " "

    if pol[0] == "+":
        return pol[2:-4]
    else:
        return pol[:-4]
    

def PolinomialDerivative(polinomial):
    dividedpol = dividePolinomial(polinomial)
    derivative = ""
    for i in dividedpol.keys():
        if dividedpol[i] != 0:
            if i[:i.index("X")] == "":
                derivative += dividedpol[i] + "x^" + str(int(dividedpol[i])-1) + " "
            else:
                derivative += str((float(i[:i.index("x")])*float(dividedpol[i]))) + "x^" + str(int(dividedpol[i])-1) + " "
    print(derivative)


def GraphPolinomial(polinomial):
    dividedpol = dividePolinomial(polinomial)
    coefs = list()
    max = 0
    policoefs = list()
    xs = np.linspace(0,9,10)
    for i in dividedpol.values():
        policoefs.append(int(i))

    for i in dividedpol.values():
        if int(i) > max:
            max = int(i)

    for i in range(max + 1):
        if i in policoefs:
            for j in dividedpol.keys():
                if int(dividedpol[j]) == i:
                    if dividedpol[j] == 0:
                        coefs.append(float(j))
                    elif j[:j.index("x")] == "":
                        coefs.append(float(1))
                    else:
                        coefs.append(float(j[:j.index("X")]))
        else:
            coefs.append(0)

    order = len(coefs)

    ys = np.zeros(len(xs))

    for i in range (order):
        ys += coefs[i] * xs ** i

    plt.plot(xs,ys)
    plt.axhline(y=0,color="r")
    plt.axvline(x=0,color="r")
    plt.show()


def FindDegree(polinomial):
    dividedpol = dividePolinomial(polinomial)
    max = 0
    for i in dividedpol.values():
        if int(i) > max:
            max = int(i)
    return max


def main():
    polinomios = LoadPolinomials("C:/Users/marti/OneDrive/polinomios.txt")
    print("Polinomios", end=" "*20)
    print("Grau")
    for i in polinomios:
        print(i,end=" "*(33-len(i)))
        print(FindDegree(i))





main()
    