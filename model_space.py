# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:51:13 2019

@author: iA
"""

#model.py gives money to random agents
#https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html


import random
from mesa import Agent, Model
from mesa.time import RandomActivation #for the scheduler. There are many schedulers available, this one is for random activation of all agents
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

#for the agents
#give each agent a unique ID, always
class MoneyAgent(Agent):
    """an agent with a fixed initial wealth"""
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model) #goes to the init of the class Agent, in the mesa library. Inheritance is used here
        self.wealth = 1 #agent with one attribute, wealth
        
    def step(self):
        #the agent's step or action goes here, I guess
        #print(self.unique_id)
        self.move()
        if self.wealth > 0:
            self.advance()
            self.give_money()
# =============================================================================
#         if self.wealth == 0:
#             return
#         other_agent = random.choice(self.model.schedule.agents)
#         other_agent.wealth += 1
#         self.wealth -=1
#      
# =============================================================================
    def advance(self):
        pass
        #self.give_money()
    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos,moore = False, include_center = False)
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self,new_position)
        
    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len (cellmates) > 1:
            other = random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1 
            
            
# =============================================================================
# 
#just a function here
#use functions like this one here outside the main classes for the ABM.
#Use classes just for defining how agents interact.
def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x  = sorted(agent_wealths)
    N = model.num_agents
    B = sum(xi * (N-i) for i,xi in enumerate(x))/(N*sum(x))
    return(1+(1/N)-2*B)


#**************************************************************************
       
#for the main model        
class MoneyModel(Model):
    """A model with some number of agents"""
    def __init__(self,N,width,height):
        self.running = True
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        #self.schedule = RandomActivation(self)
        self.schedule = SimultaneousActivation(self)
        #create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i,self) #i becomes the unique id. Use of self here is still a question...
            self.schedule.add(a)
            
            #adding agent to a random grid cell
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a,(x,y))
        
        self.datacollector = DataCollector(
                model_reporters = {"Gini": compute_gini,"Number": "num_agents"},   #a function to call
                agent_reporters = {"Wealth": "wealth"})        #agent attribute
        
    def step(self):
        '''Ádvance the model by one step'''
        self.datacollector.collect(self)
        self.schedule.step() #it shuffles the order of the agents, then activates them all, one at a time.
        #print(self.unique_id)
        #print(a.wealth)
        
        
        
        

# =============================================================================
# 
#empty_model = MoneyModel(10) #initialize model with N = 10
#empty_model.step()#running the model for one step
#  
# =============================================================================

# =============================================================================
#TIME - mesa has a scheduler
#
# The scheduler is a special model component which controls the order in which agents are activated.
# For example, all the agents may activate in the same order every step; their order might be shuffled;
# we may try to simulate all the agents acting at the same time; and more.
# Mesa offers a few different built-in scheduler classes, with a common interface.
# That makes it easy to change the activation regime a given model uses, and see whether it changes the model behavior.
# This may not seem important, but scheduling patterns can have an impact on your results [Comer2014]_.            
#         
# =============================================================================

        
        