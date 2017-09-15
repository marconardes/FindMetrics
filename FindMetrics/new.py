#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:20:18 2017

@author: home
"""

import plotly.plotly as py
import plotly.graph_objs as go

x = ['1', '1', '1','2', '2', '2']

trace0 = go.Box(
    y=[0.2, 0.2, 0.6, 1.0, 0.5, 0.4],
    x=x,
    name='kale',
    marker=dict(
        color='#3D9970'
    )
)
trace1 = go.Box(
    y=[0.6, 0.7, 0.3, 0.6, 0.0, 0.5],
    x=x,
    name='radishes',
    marker=dict(
        color='#FF4136'
    )
)

data = [trace0, trace1]
layout = go.Layout(
    yaxis=dict(
        title='normalized moisture',
        zeroline=False
    ),
    boxmode='group'
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig)