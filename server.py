# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:56:19 2019

@author: iA
"""

#server.py

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from model_space import MoneyModel
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter

def agent_portrayal(agent):
    portrayal = {"x": 5,
                 "y": 5,
                 "Shape": "circle",
                 "Filled" : "true",
                 "r": 0.5}
    
    if agent.wealth>0:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
            
    return portrayal

grid = CanvasGrid(agent_portrayal,10,10,500,500)

n_slider = UserSettableParameter('slider',"Number of Agents",100,2,200,1)

chart1 = ChartModule([{"Label": "Gini",
                      "Color": "Black"}],
                    data_collector_name='datacollector')


chart2 = ChartModule([{"Label": "Number",
                      "Color": "Red"}],
                    data_collector_name='datacollector')


server = ModularServer(MoneyModel,
                       [grid, chart1, chart2],
                       "Money Model",
                       {"N": n_slider, "width": 10, "height": 10})