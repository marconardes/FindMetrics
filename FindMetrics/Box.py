#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:34:15 2017

@author: home



"""

import seaborn as sns
import pandas as pd

def plotBar(hash,figname,a, b,c):
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
    tips = sns.load_dataset("tips")
    ax = sns.boxplot(x="INCREMENTO", y="TASK", hue="TIPO", data=pdd, palette="Set3")
    ax.get_figure().savefig(figname)


hashmap = {'/home/home/git/exp1groupBsub4': [137, 90, 25, 174, 26, 63, 43, 83, 14, 60], '/home/home/git/Piloto_Nardes': [148, 92, 20, 67, 206, 100, 114, 7, 213, -4], '/home/home/git/Piloto_Guerra': [97, 58, 22, 56, 54, 56, 29, 51, 67, 30], '/home/home/git/exp1groupAsub2': [78, 57, 127, 44, 29, 36, 18, -5, 40, 25], '/home/home/git/exp1groupBsub2': [161, 114, 23, 131, 171, 228, 151, 63, 117, 55]}

plotBar(hashmap)