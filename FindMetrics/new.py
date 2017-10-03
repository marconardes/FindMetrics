import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def readCsv():
    listCsv = pd.read_csv('devs.csv')
    return listCsv

def newDataFrame(lista):
    print "INICIANDO"
    i = 1
    res = pd.DataFrame(columns=('Experimento', 'Task','Loc'))
    
    l=0
    contador = len(lista)    
    arr = []
    print arr
    for x in range(0, contador):
        if "Nardes" in lista["diretorio"][x]:
            arr.append("With Metadata")
            arr.append("Task"+str(i))
            arr.append(lista['Loc'][x])
            res.loc[x]=arr
            arr=[]
            if(i == 10):
                i = 0
            i =  i+1
        
        if "exp1groupB" in lista["diretorio"][x]:
            arr.append("With Metadata")
            arr.append("Task"+str(i))
            arr.append(lista['Loc'][x])
            res.loc[x]=arr
            arr=[]
            if(i == 10):
                i = 0
            i =  i+1
        if "Guerra" in lista["diretorio"][x]:
            arr.append("Winouth Metadata")
            arr.append("Task"+str(i))
            arr.append(lista['Loc'][x])
            res.loc[x]=arr
            arr=[]
            if(i == 10):
                i = 0
            i =  i+1
        if "exp1groupA" in lista["diretorio"][x]:
            arr.append("Winouth Metadata")

            arr.append("Task"+str(i))
            arr.append(lista['Loc'][x])
            res.loc[x]=arr
            arr=[]
            if(i == 10):
                i = 0
            i =  i+1
    print res
    return res
    

listaCsv = readCsv()

serie = newDataFrame(listaCsv)

#series = pd.Series(df)

sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
ax = sns.boxplot(x="Loc", y="Task", hue="Experimento",data=serie)
ax.get_figure().savefig('ax.png')
