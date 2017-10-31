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
    listCsv = pd.read_csv('csv/tarefas.csv')
    return listCsv


def readCsvFinal():
    listCsv = pd.read_csv('csv/final.csv')
    return listCsv

def respost(csv):
    contador = len(csv)
    valor =[]
    print contador
    for x in range(0, contador):
            valor.append('Carimbo de data/hora')
            valor.append(csv['Carimbo de data/hora'][x])
            
            valor.append('Nome')
            valor.append(csv['Nome'][x])
                
            valor.append('Grupo do Experimento')
            valor.append(csv['Grupo do Experimento'][x])
            
            valor.append('Houve alguma decisão tomada nas primeiras tarefas que precisou ser refatorada posteriormente? Em caso positivo descreva quais.')
            valor.append(csv['Houve alguma decisão tomada nas primeiras tarefas que precisou ser refatorada posteriormente? Em caso positivo descreva quais.'][x])
            
            valor.append('Descreva quais tarefas puderam ser realizadas de forma simples durante o experimento.')
            valor.append(csv['Descreva quais tarefas puderam ser realizadas de forma simples durante o experimento.'][x])
            
            valor.append('Descreva quais tarefas puderam ser realizadas de forma simples durante o experimento.')
            valor.append(csv['Descreva quais tarefas puderam ser realizadas de forma simples durante o experimento.'][x])

            valor.append('Quais funcionalidades do Esfinge Metadata você utilizou?')
            valor.append(csv['Quais funcionalidades do Esfinge Metadata você utilizou?'][x])

            valor.append('Descreva os principais benefícios que você enxergou no uso do Esfinge Metadata')
            valor.append(csv['Descreva os principais benefícios que você enxergou no uso do Esfinge Metadata'][x])

            valor.append('Descreva as principais desvantagens que você enxergou no uso do Esfinge MetadataDescreva as principais desvantagens que você enxergou no uso do Esfinge Metadata')
            valor.append(csv['Descreva as principais desvantagens que você enxergou no uso do Esfinge Metadata'][x])

            valor.append('Sobre a frase "Eu utilizaria o Esfinge Metadata na implementação de um framework"')
            valor.append(csv['Sobre a frase "Eu utilizaria o Esfinge Metadata na implementação de um framework"'][x])

            valor.append('Justifique sua resposta anterior')
            valor.append(csv['Justifique sua resposta anterior'][x])         
            
            valor.append("==================================")
            
    return valor

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



final = respost(readCsvFinal())

with open('csv/Tempo.csv','wb') as f:
    w = csv.writer(f)
    w.writerows(formato.items())


with open("csv/Relatorios.txt", "w") as text_file:
    for x in formated:
            z = str(x)
            text_file.write(z)
            text_file.write("\n")
            

with open("csv/RelatorioFinal.txt", "w") as text_file:
    for x in final:
            z = str(x)
            text_file.write("\n")
            text_file.write(z)
            text_file.write("\n")


