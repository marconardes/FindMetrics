#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# encoding: utf-8
#coding: utf-8

"""
Created on Wed Sep 27 10:33:03 2017

@author: home
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv as csv


def readCsv():
    listCsv = pd.read_csv('Relato.csv')
    return listCsv


def formatText(csv):
    contador = len(csv)
    valor = []
    for x in range(0, contador):
        if(x==0):
            valor.append(csv['Nome'][x])
            valor.append(csv['Grupo'][x])
            valor.append("TASK ")
            valor.append(csv['Tarefa'][x])
            valor.append("IMPLEMENTAÇÃO")
            valor.append(csv['IMPL'][x])
            valor.append("DIFICULDADES")
            valor.append(csv['DIFIC'][x])
            valor.append("\n")

        elif(x<contador-1):
            if( csv['Nome'][x]==csv['Nome'][x+1]):
                valor.append("TASK ")
                valor.append(csv['Tarefa'][x])
                valor.append("IMPLEMENTAÇÃO")
                valor.append(csv['IMPL'][x])
                valor.append("DIFICULDADES")
                valor.append(csv['DIFIC'][x])
                valor.append("\n")
                
            else:
                valor.append("TASK ")
                valor.append(csv['Tarefa'][x])
                valor.append("IMPLEMENTAÇÃO")
                valor.append(csv['IMPL'][x])
                valor.append("DIFICULDADES")
                valor.append(csv['DIFIC'][x])
                valor.append("\n")
                valor.append("============================================")
                valor.append(csv['Nome'][x+1])
                valor.append(csv['Grupo'][x+1])
               
        else:
                valor.append("TASK ")
                valor.append(csv['Tarefa'][x])
                valor.append("IMPLEMENTAÇÃO")
                valor.append(csv['IMPL'][x])
                valor.append("DIFICULDADES")
                valor.append(csv['DIFIC'][x])
                valor.append("\n")
            
    return valor

def newFormat(csv):
    
    formato = {}
    valor = []
    contador = len(csv)
    print contador
    for x in range(0, contador):
        print x
        if(x<contador-1):
            if( csv['Nome'][x]==csv['Nome'][x+1]):
                valor.append(csv['Tempo'][x])
                print valor
            else:
                valor.append(csv['Tempo'][x])
                formato[csv['Nome'][x]+","+csv['Grupo'][x]]= valor                
                valor = []
               
        else:
            valor.append(csv['Tempo'][x])
            formato[csv['Nome'][x]+","+csv['Grupo'][x]]= valor
            print valor
            valor = []

    return formato

relatorio = readCsv()

formato = newFormat(relatorio)

formated = formatText(relatorio)

with open('Tempo.csv','wb') as f:
    w = csv.writer(f)
    w.writerows(formato.items())


with open("Relatorios.txt", "w") as text_file:
    for x in formated:
            z = str(x)
            print z
            text_file.write(z)
            text_file.write("\n")
