#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:34:15 2017

@author: home





"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def freatureBoxGraf(Dados,savef):
    pdd = pd.DataFrame(columns=["Group", "Type", "LOC"])
    for key, value in Dados.items():
        for x in range(0, len(value)):
            if (x == 0):
                nome = "Start framework structure"
                valor = value[x]
                adicionaNoCerto(key, nome, valor, pdd)
            elif ((x == 1) or (x == 3) or (x == 9)):
                nome = "New mapping annotation"
                valor = value[x]
                adicionaNoCerto(key, nome, valor, pdd)
            elif ((x == 2) or (x == 4) or (x == 5)):
                nome = "Data validation"
                valor = value[x]
                adicionaNoCerto(key, nome, valor, pdd)
            elif ((x == 6) or (x == 8)):
                nome = "Feature enhancement"
                valor = value[x]
                adicionaNoCerto(key, nome, valor, pdd)
            elif (x == 7):
                nome = "Extension point"
                valor = value[x]
                adicionaNoCerto(key, nome, valor, pdd)
        
        sns.set_style("whitegrid")
        flatui = ["#99bbff", "#ff8080"]
        sns.set_palette(flatui)
        plt.figure(figsize=(14, 12))
        ax = sns.boxplot(x="LOC", y="Type", hue="Group", data=pdd)
        ax.get_figure().savefig(savef)
        ax.get_figure().clf()


def adicionaNoCerto(key,nome,valor,dataFrame):
    
    if "Nardes" in key:
         dataFrame.loc[len(pdd)] = ['With Metadata', nome, value[x]]
    elif "Guerra" in key:
         dataFrame.loc[len(pdd)] = ['Without Metadata', nome, value[x]]
    elif "exp1groupA" in key:
         dataFrame.loc[len(pdd)] = ['Without Metadata', nome, value[x]]
    elif "exp1groupB" in key:
         dataFrame.loc[len(pdd)] = ['With Metadata', nome, value[x]]

    return dataFrame


freatureBoxGraf(z)

    
    