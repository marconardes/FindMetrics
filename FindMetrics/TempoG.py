#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:23:40 2017

@author: home
"""
import csv
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


listCsv =[]

def readCsv():
    with open('Tempo.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            listCsv.append(row)




def toDict(lista):
    dados = {}
    tamanho = len(lista)
    for x in range(0, tamanho): 
        sublist = lista[x]
        tamanhoSub = len(sublist)
        value=[]
        for z in range(0, tamanhoSub):
            if(z >0):
                value.append(float(sublist[z]))
                

        dados.setdefault(sublist[0] + str(x),value)
    return dados
    
def totalTime(lista):
    dados = {}
    print "nao implementado"
    for key, value in lista.items():
        print key
        print value
        tamanho = len(value)
        valueIncr = []
        n =0
        
        for x in range(0, tamanho):
             n = value[x]+n
             valueIncr.append(n)
        print valueIncr      
        dados.setdefault(key,valueIncr)  
    return dados
    


def plotBarGraf(hash,figname,a, b,c):
    pdd = pd.DataFrame(columns=[a, b,c])
    print pdd
    for key, value in hash.items():
        for x in range(0, len(value)):
            y = x + 1
            if "Metadata" in key:
                pdd.loc[len(pdd)] = ['With Metadata', "Task " + str(y), value[x]]
            elif "Reflection" in key:
                pdd.loc[len(pdd)] = ['Without Metadata', "Task " + str(y), value[x]]
    
    sns.set_style("whitegrid")

    flatui = ["#99bbff", "#ff8080"]
    sns.set_palette(flatui)
    ax = sns.boxplot(x=c, y=b, hue=a, data=pdd)
    ax.get_figure().savefig(figname)
    ax.get_figure().clf()
    


def plotTime(hashMap,labelx,labely,name):
    m = 0
    i = 0
    for key, value in hashMap.items():
        if ("Metadata" in key) and (m==0):
            plt.plot(value, label="With Metadata", color='Red')
            m=1
        elif ("Reflection" in key)and(i==0):
            plt.plot(value, label="Without Metadata", color='Blue')
            i=1
        if ("Metadata" in key) and (m==1):
            plt.plot(value,  color='Red')
            m=1
        elif ("Reflection" in key)and(i==1):
            plt.plot(value,  color='Blue')
            i=1
        plt.legend()
    
    plt.ylabel(labely)
    plt.xlabel(labelx)
    plt.savefig("timeLine/"+name)
    plt.close()

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
    
    if "Metadata" in key:
         dataFrame.loc[len(dataFrame)] = ['With Metadata', nome,valor]
    elif "Reflection" in key:
         dataFrame.loc[len(dataFrame)] = ['Without Metadata', nome, valor]

    return dataFrame





readCsv()

dic = toDict(listCsv)
plotTime(dic,"Task","Time","timeIncrement.png")
plotBarGraf(dic,"timeLine//incrTime.png","TYPE","TASK","TIME")
freatureBoxGraf(dic,"time.png"," Tempo")



incr = totalTime(dic)
plotTime(incr,"Task","Time","timeLine.png")
plotBarGraf(dic,"timeLine//boxTime.png","TYPE","TASK","TIME")

