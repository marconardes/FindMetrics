#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import csv
import numpy as np
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
        x = key.split('/')
        if "Nardes" in key:
            plt.plot(value, label="Com Metadata", color='Red')
        elif "Guerra" in key:
            plt.plot(value, label="Sem Metadata", color='Blue')
        elif "exp1groupA" in key:
            plt.plot(value, color='Blue')
        elif "exp1groupB" in key:
            plt.plot(value,  color='Red')
        plt.legend()
    
    plt.ylabel(labely)
    plt.xlabel(labelx)
    plt.show()


def calcularMedia(hashElement):
    print"nao implementado"
    i = 0
    list = []
    
    for key, value in hashElement.items():
        list.append(value)
        i=i+1
    
    arr = list[0]
    
    for x in range(1, len(list)):
        for z in range(0, len(list[x])):
            arr[z]= arr[z] +list[x][z]
        
    
    for x in range(0, len(arr)):
        arr[x] = arr[x]/i
    return arr
    

def calcularDp(hashElement):
    print"nao implementado"
    
    a = []
    
    #a =[[1,2,3],[1,2,3]]
    
    c  = 0
    
    for key, value in hashElement.items():
        print value
        a[c].append(value)        
        c = c+1
    
    aInv = []
    
    print len(aInv)
    
    print len(a)
    
    for x in range(0, len(aInv)):
        print "x    "+ str(x)    
        value = []
        for y in range(0, len(a)):
            print "YYYYY   "+str(y)
            b = a[y]
            
            #print(b)
            value.append(b[x])
        print value
        aInv[x].append(value)
    
    print aInv
    return aInv

    

def plotBarGraf(hash,figname,a, b,c):
    pdd = pd.DataFrame(columns=[a, b,c])
    for key, value in hash.items():
        for x in range(0, len(value)):
            y = x + 1
            if "Nardes" in key:
                pdd.loc[len(pdd)] = ['Com Metadata', "Task " + str(y), value[x]]
            elif "Guerra" in key:
                pdd.loc[len(pdd)] = ['Sem Metadata', "Task " + str(y), value[x]]
            elif "exp1groupA" in key:
                pdd.loc[len(pdd)] = ['Sem Metadata', "Task " + str(y), value[x]]
            elif "exp1groupB" in key:
                pdd.loc[len(pdd)] = ['Com Metadata', "Task " + str(y), value[x]]
    
    sns.set_style("whitegrid")

    flatui = ["#99bbff", "#ff8080"]
    sns.set_palette(flatui)
    #sns.palplot(sns.color_palette())    
    ax = sns.boxplot(x=c, y="TASK", hue="TIPO", data=pdd)
    ax.get_figure().savefig(figname)
    ax.get_figure().clf()

    
    
    

listCsv = list()
hashMap={}
ReadCsv(listCsv)
tamanho = len(listCsv)
getFieldList(listCsv, list, hashMap, tamanho, 2)
plotLineGraf(hashMap,"Commits","Loc")

hashMap2={}
getFieldList(listCsv, list, hashMap2, tamanho, 3)
plotLineGraf(hashMap2,"Commits","WMC")


plotBarGraf(hashMap,"loc.png","TIPO","TASK","LOC")

plotBarGraf(hashMap2,"wmc.png","TIPO","TASK","WMC")
