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



#for the agents
#give each agent a unique ID, always
class MoneyAgent(Agent):
    """an agent with a fixed initial wealth"""
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model) #goes to the init of the class Agent, in the mesa library. Inheritance is used here
        self.wealth = 1 #agent with one attribure, wealth
        
        
    def step(self):
        #the agent's step or action goes here, I guess
        
        print(self.unique_id, self.wealth)
        #print(self.wealth)
        print(self.unique_id)
        if self.wealth == 0:
            return
        other_agent = random.choice(self.model.schedule.agents)
        other_agent.wealth += 1
        self.wealth -=1
        
    

#for the main model        
class MoneyModel(Model):
    """A model with some number of agents"""
    def __init__(self,N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        #create agents
        for i in range(self.num_agents):
            #here is the agent definition
            a = MoneyAgent(i,self) #i becomes the unique id. Use of self here is still a question...
            self.schedule.add(a)
        
        
                
    def step(self):
        '''Ádvance the model by one step'''
        #print(self.num_agents)
      
        self.schedule.step() #it shuffles the order of the agents, then activates them all, one at a time.
        #print(self.unique_id)
# =============================================================================
# 
empty_model = MoneyModel(10) #initialize model with N = 10
empty_model.step()#running the model for one step
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

        
        