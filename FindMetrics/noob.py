#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 12:56:38 2017

@author: home
"""
import csv
import matplotlib.pyplot as plt


listCsv = list()


with open('devs.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        listCsv.append(row)

tamanho = len(listCsv)

for x in range(0, tamanho):
    if(x==tamanho-1):  
        print x, listCsv[x]
    elif (listCsv[x][0] == listCsv[x+1][0]):
        print 'true'
    else:
        print 'false'