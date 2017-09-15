#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:34:15 2017

@author: home
"""

import plotly 

import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
plotly.tools.set_credentials_file(username='marconardes', api_key='PTzNuvMveK5p8j7glJCl')

y0 = [148.0, 161.0, 148.0]
y1 = [87.0,78.0,60]

trace0 = go.Box(
    y=y0
)
trace1 = go.Box(
    y=y1
)
trace2 = go.Box(
    y=y1
)
data = [trace0, trace1,trace2]
py.plot(data)