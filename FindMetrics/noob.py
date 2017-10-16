#!/usr/bin/env python2
# -*- coding: utf-8 -*-
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
            obj.append(int(listCsv[x][n]))
            hashMap.setdefault(listCsv[x][0], obj)
        elif (listCsv[x][0] == listCsv[x + 1][0]):
            obj.append(int(listCsv[x][n]))
        else:
            obj.append(int(listCsv[x][n]))
            hashMap.setdefault(listCsv[x][0], obj)
            obj = list()

def plotLineGraf(hashMap,labelx,labely):
    for key, value in hashMap.items():
        if "Nardes" in key:
            plt.plot(value, label="With Metadata", color='Red')
        elif "Guerra" in key:
            plt.plot(value, label="Without Metadata", color='Blue')
        elif "exp1groupA" in key:
            plt.plot(value, color='Blue')
        elif "exp1groupB" in key:
            plt.plot(value,  color='Red')
        plt.legend()
    
    plt.ylabel(labely)
    plt.xlabel(labelx)
    plt.show()


def generateIncrement(hashMap):
    dic ={}
    for key, value in hashMap.items():
        obj = list()
        tamanho = len(value)
        for x in range(0, tamanho):
            if x>0:
                obj.append(value[x]-value[x-1])
            else:
                obj.append(value[x])
       
        dic.setdefault(key, obj)
        
    return dic
    

def plotBarGraf(hash,figname,a, b,c):
    pdd = pd.DataFrame(columns=[a, b,c])
    for key, value in hash.items():
        for x in range(0, len(value)):
            y = x + 1
            if "Nardes" in key:
                pdd.loc[len(pdd)] = ['With Metadata', "Task " + str(y), value[x]]
            elif "Guerra" in key:
                pdd.loc[len(pdd)] = ['Without Metadata', "Task " + str(y), value[x]]
            elif "exp1groupA" in key:
                pdd.loc[len(pdd)] = ['Without Metadata', "Task " + str(y), value[x]]
            elif "exp1groupB" in key:
                pdd.loc[len(pdd)] = ['With Metadata', "Task " + str(y), value[x]]
    
    sns.set_style("whitegrid")

    flatui = ["#99bbff", "#ff8080"]
    sns.set_palette(flatui)
    ax = sns.boxplot(x=c, y="TASK", hue="TIPO", data=pdd)
    ax.get_figure().savefig(figname)
    ax.get_figure().clf()
    
def xdivy(hash1,hash2):
    f={}

    for key, value in hash1.items():
        n=[]
        value2 = hash2.get(key)
        for x in range(0, len(value)):
            z = float(value[x])/float(value2[x])
            n.append(z)
        
        f.setdefault(key,n)        
    return f
    

listCsv = list()

loc={}

ReadCsv(listCsv)
tamanho = len(listCsv)
getFieldList(listCsv, list, loc, tamanho, 2)
plotLineGraf(loc,"Commits","Loc")
plotBarGraf(loc,"Box/loc.png","TIPO","TASK","LOC")



wmc={}
getFieldList(listCsv, list, wmc, tamanho, 3)
plotLineGraf(wmc,"Commits","WMC")
plotBarGraf(wmc,"Box/wmc.png","TIPO","TASK","WMC")

cbo={}
getFieldList(listCsv, list, cbo, tamanho, 4)
plotLineGraf(wmc,"Commits","CBO")
plotBarGraf(wmc,"Box/cbo.png","TIPO","TASK","CBO")

lcom={}
getFieldList(listCsv, list, lcom, tamanho, 5)
plotLineGraf(wmc,"Commits","LCOM")
plotBarGraf(wmc,"Box/lcom.png","TIPO","TASK","LCOM")

nom={}
getFieldList(listCsv, list, nom, tamanho, 5)
plotLineGraf(wmc,"Commits","NOM")
plotBarGraf(wmc,"Box/nom.png","TIPO","TASK","NOM")

nof={}
getFieldList(listCsv, list, nof, tamanho, 6)
plotLineGraf(wmc,"Commits","NOF")
plotBarGraf(wmc,"Box/nof.png","TIPO","TASK","NOF")

wmcxnom = xdivy(wmc,nom)


incrementoLoc = generateIncrement(loc)
incrementoCbo = generateIncrement(cbo)
incrementoLcom = generateIncrement(lcom)
incrementoNom = generateIncrement(nom)
incrementoNof = generateIncrement(nof)


plotBarGraf(incrementoLoc,"Incremento/incrementoLoc.png","TIPO","TASK","INCREMENTO LOC")
plotBarGraf(incrementoCbo,"Incremento/incrementoCbo.png","TIPO","TASK","INCREMENTO CBO")
plotBarGraf(incrementoLcom,"Incremento/incrementoLcom.png","TIPO","TASK","INCREMENTO LCOM")
plotBarGraf(incrementoNom,"Incremento/incrementoNom.png","TIPO","TASK","INCREMENTO NOM")
plotBarGraf(incrementoNof,"Incremento/incrementoNof.png","TIPO","TASK","INCREMENTO NOF")




plotBarGraf(wmcxnom,"wmcxnom.png","TIPO","TASK","wmcxnom")
plotLineGraf(wmcxnom,"Commits","wmcxnom")