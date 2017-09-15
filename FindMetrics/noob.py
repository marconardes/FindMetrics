#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import csv
import numpy as np
import matplotlib.pyplot as plt

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
            plt.plot(value, label=x[4], color='green')
        elif "Guerra" in key:
            plt.plot(value, label=x[4], color='blue')
        elif "exp1groupA" in key:
            plt.plot(value, label=x[4], color='blue')
        elif "exp1groupB" in key:
            plt.plot(value, label=x[4], color='green')
        plt.legend()
    
    plt.ylabel(labely)
    plt.xlabel(labelx)
    plt.show()

def separavalores(hashMap,hashSemMetadata,hashComMetadata):
    for key, value in hashMap.items():
        if "Nardes" in key:
            hashComMetadata.setdefault(key,value)
        elif "Guerra" in key:
            hashSemMetadata.setdefault(key,value)
        elif "exp1groupA" in key:
            hashSemMetadata.setdefault(key,value)
        elif "exp1groupB" in key:
            hashComMetadata.setdefault(key,value)


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

    

    
def formatBarGraf(hashMap):
    print "nao implementado"

def plotBarGraf(hashMap):
    print "nao implementado"
    
    
    
hashSemMetadata={}
hashComMetadata={}

listCsv = list()
hashMap={}
ReadCsv(listCsv)
tamanho = len(listCsv)
getFieldList(listCsv, list, hashMap, tamanho, 2)
plotLineGraf(hashMap,"Commits","Loc")
formatBarGraf(hashMap)

hashMap2={}
getFieldList(listCsv, list, hashMap2, tamanho, 3)
plotLineGraf(hashMap2,"Commits","WMC")

separavalores(hashMap,hashSemMetadata,hashComMetadata)

mediaComMetadata = calcularMedia(hashComMetadata)
mediaSemMetadata = calcularMedia(hashSemMetadata)
#PLOT DAS MEDIAS
plt.plot(mediaComMetadata, label="label", color='blue')
plt.plot(mediaSemMetadata, label="label", color='red')

#CALCULO DO DESVIO PADRAO
dpComMetadata = calcularDp(hashComMetadata)


