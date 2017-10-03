import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd


def ReadCsv(listCsv):
    with open('devs.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            listCsv.append(row)


def getFieldList(listCsv, list, hashMap, tamanho, n):
    obj = list()
    print tamanho
    for x in range(0, tamanho):
        if (x == tamanho - 1):
            obj.append(listCsv[x][n])
            hashMap.setdefault(listCsv[x][0], obj)
        elif (listCsv[x][0] == listCsv[x + 1][0]):
            obj.append(listCsv[x][n])
        else:
            obj.append(listCsv[x][n])
            hashMap.setdefault(listCsv[x][0], obj)
            obj = list()


def plotBarGraf(hashMap):
    print "nao implementado"



#listCsv = list()
#hashMap={}
#ReadCsv(listCsv)
#tamanho = len(listCsv)
#getFieldList(listCsv, list, hashMap, tamanho, 2)
#formatBarGraf(hashMap)
#plotBarGraf(hashMap)
    
 
# data to plot


datos = [[1, 2, 3, 4], [3, 5, 3, 5], [8, 6, 4, 2], [8, 6, 4, 2]]
X = np.arange(4)
plt.bar(X + 0.00, datos[0], color = "b", width = 0.25)
plt.bar(X + 0.25, datos[1], color = "g", width = 0.25)
plt.bar(X + 0.50, datos[2], color = "r", width = 0.25)
plt.bar(X + 0.75, datos[3], color = "y", width = 0.25)
plt.xticks(X+0.38, ["A","B","C","D"])
