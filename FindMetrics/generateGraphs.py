#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import seaborn as sns
import pandas as pd

groupName = "groupAsub7" #high loc step - reflection P7
groupName2 = "groupBsub10" #high loc step - metadata P4

def ReadCsv(listCsv):
    with open('final.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            listCsv.append(row)
            
def getFieldList(listCsv, list, hashMap, tamanho, n):
    obj = list()
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
    #print(hashMap)

def plotLineGraf(hashMap,labelx,labely,name):
    
    i=0
    n=0
    for key, value in hashMap.items():
        x = key.split('/')
        if groupName in key:
            plt.plot(value, color='Blue', linestyle='--')
        elif groupName2 in key:
            plt.plot(value, color='Red', linestyle='--')
        elif "exp1groupB" in key:
            plt.plot(value, color='Red')
        elif "exp1groupA" in key:
            plt.plot(value, color='Blue')
        #elif "exp1groupA" in key:
        #    plt.plot(value, color='Blue')
        #elif "exp1groupB" in key:
        #    plt.plot(value,  color='Red')
        #plt.legend()
    
    #plt.figlegend( lines, labels, loc = 'lower center', ncol=5, labelspacing=0. #)
    
    red_patch = mpatches.Patch(color='red', label='With Metadata')
    blue_patch = mpatches.Patch(color='blue', label='Pure Java Reflection')
    blue_dashedPatch = mpatches.Patch(color='blue',fill=False, linestyle='--', label='Participant 7 (P7)')
    red_dashedPatch = mpatches.Patch(color='red',fill=False, linestyle='--',label='Participant 4 (P4)')
    plt.legend(handles=[red_patch,blue_patch,blue_dashedPatch,red_dashedPatch], loc=2)

    plt.ylabel(labely)
    plt.xlabel(labelx)
    plt.xticks(np.arange(10),np.arange(1,11))
    #plt.show()
    plt.savefig("../"+groupName+"/"+labely+"Line.png")
    plt.clf()

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
    print pdd
   
    for key, value in hash.items():
        for x in range(0, len(value)):
            y = x + 1
            if "exp1groupA" in key:
                pdd.loc[len(pdd)] = ['Pure Java Reflection', "Task " + str(y), value[x]]
            elif "exp1groupB" in key:
                pdd.loc[len(pdd)] = ['With Metadata', "Task " + str(y),       value[x]]
    sns.set_style("whitegrid")
    flatui = ["#ff8080", "#99bbff"] 
    sns.set_palette(flatui)
    ax = sns.boxplot(x=c, y="TASK", hue="TIPO", data=pdd)
    ax.get_figure().savefig("../"+groupName+"/"+figname + "-BAR.png")
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

def freatureBoxGraf(Dados,savef,c):
    dados = pd.DataFrame(columns=["Group", "Type", c])
    for key, value in Dados.items():
        for x in range(0, len(value)):
            if (x == 0):
                nome = "Start framework structure"
                valor = value[x]
                adicionaNoCerto(key, nome, valor, dados)
            elif ((x == 1) or (x == 3) or (x == 9)):
                nome = "New mapping annotation"
                valor = value[x]
                adicionaNoCerto(key, nome, valor, dados)
            elif ((x == 2) or (x == 4) or (x == 5)):
                nome = "Data validation"
                valor = value[x]
                adicionaNoCerto(key, nome, valor, dados)
            elif ((x == 6) or (x == 8)):
                nome = "Feature enhancement"
                valor = value[x]
                adicionaNoCerto(key, nome, valor, dados)
            elif (x == 7):
                nome = "Extension point"
                valor = value[x]
                adicionaNoCerto(key, nome, valor, dados)
        
        sns.set_style("whitegrid")
        flatui = ["#99bbff", "#ff8080"]
        sns.set_palette(flatui)
        plt.figure(figsize=(14, 12))
        print c
        ax = sns.boxplot(x=c, y="Type", hue="Group", data=dados)
        ax.get_figure().savefig(savef)
        ax.get_figure().clf()


def adicionaNoCerto(key,nome,valor,dataFrame):
    
    if "Nardes" in key:
         dataFrame.loc[len(dataFrame)] = ['With Metadata', nome,valor]
    elif "Guerra" in key:
         dataFrame.loc[len(dataFrame)] = ['Without Metadata', nome, valor]
    elif "exp1groupA" in key:
         dataFrame.loc[len(dataFrame)] = ['Without Metadata', nome, valor]
    elif "exp1groupB" in key:
         dataFrame.loc[len(dataFrame)] = ['With Metadata', nome, valor]

    return dataFrame



  

listCsv = list()

loc={}
plt.figure(figsize=(14, 12))

ReadCsv(listCsv)
tamanho = len(listCsv)
getFieldList(listCsv, list, loc, tamanho, 2)
plotLineGraf(loc,"Commits","Loc")
plotBarGraf(loc,"loc","TIPO","TASK","LOC")

plt.close("all")
wmc={}
getFieldList(listCsv, list, wmc, tamanho, 3)
plotLineGraf(wmc,"Commits","WMC")
#plotBarGraf(wmc,"wmc","TIPO","TASK","WMC")

cbo={}
getFieldList(listCsv, list, cbo, tamanho, 4)
plotLineGraf(cbo,"Commits","CBO")
plotBarGraf(cbo,"cbo","TIPO","TASK","CBO")

lcom={}
getFieldList(listCsv, list, lcom, tamanho, 5)
plotLineGraf(lcom,"Commits","LCOM")
plotBarGraf(lcom,"lcom","TIPO","TASK","LCOM")

nom={}
getFieldList(listCsv, list, nom, tamanho, 6)
plotLineGraf(nom,"Commits","NOM")
plotBarGraf(nom,"nom","TIPO","TASK","NOM")

nof={}
getFieldList(listCsv, list, nof, tamanho, 7)
plotLineGraf(nof,"Commits","NOF")
plotBarGraf(nof,"nof","TIPO","TASK","NOF")

ac={}
getFieldList(listCsv, list, ac, tamanho, 8)
plotLineGraf(ac,"Commits","AC")
plotBarGraf(ac,"ac","TIPO","TASK","AC")

cboNorm={}
getFieldList(listCsv, list, cboNorm, tamanho, 9)
plotLineGraf(cboNorm,"Commits","CBO-NORM")
plotBarGraf(cboNorm,"cboNorm","TIPO","TASK","CBO-NORM")


plotBarGraf(wmcxnom,"Incremento/wmcxnom.png","TIPO","TASK","wmcxnom")
plotLineGraf(wmcxnom,"Commits","wmcxnom","wmcxnom.png")
plt.close('all')

wmcxnom = xdivy(wmc,nom)
plotBarGraf(wmcxnom,"wmcxnom.png","TIPO","TASK","wmcxnom")
plotLineGraf(wmcxnom,"Commits","WMCxNOM")
