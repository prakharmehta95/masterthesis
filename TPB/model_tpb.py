# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:31:21 2019

@author: iA
"""

import random 
import pandas as pd
import numpy as np

from mesa import Agent, Model #base classes
from mesa.time import RandomActivation #for time considerations
from mesa.time import SimultaneousActivation
from mesa.datacollection import DataCollector #for data collection, of course

#commenting to see if it updates on onedrive 



class tpb_agent(Agent):
    
    def __init__(self,unique_id,model):#,attitude,network,pp):
        
        super().__init__(unique_id,model) 
        
        #self.unique_id = change_ids(self)#unique_id#instead of super I just defined it here
        #THIS IS BEST DONE WHEN THE AGENTS ARE BEING ACTIVATED IN THE MODEL CLASS - tpb IN THIS CASE
        #try to change unique_id of each agent to the zone_ids I have from the CEA
        
        
        #self.attitude = env_attitude(self) #call a function here to set attitude of each agent
        #self.network = swn(self) #call a function here to assign a list of people in network to each agent
        #self.pp = payback_period(self) #call a function to assign one number to each agent
        
    def step(self):
        '''defines what the agent does in his step'''
        print("unique id is: ",self.unique_id)
        #go to the various functions to define attitude, swn ratio, pp ratio
        #go to the intention function to see if the threshold is exceeded
        #go to the NPV ranking function and see if adoption occurs
        pass

    def otherfunctions(self):
        pass
    


class tpb(Model):
    
    #class variables - to be shared with all instances of the tpb class - go here
    #examples: weights for the intention calculation, threshold value
    threshold_intention = 0.5
    
    
    def __init__(self,N):
        super().__init__()
        self.num_agents = N
        self.schedule = RandomActivation(self) #or StagedActivation(self)?
        #agent definition:
        #instead of num_agents below, I can use the length of the dataframe I guess
        for i in test_agents_df[1:6,0]: #within the agents excel I will import; use the list of agents here #range(self.num_agents):
            #print("i is: ",i)
            a = tpb_agent(i,self)
            self.schedule.add(a)
            #in this for loop, I replace the 'i' with bldg_ids from the variable ids
        
        
    def step(self):
        self.schedule.step()



    
    
#MORE FUNCTIONS can be outside the 2 classes as welll
        
def paybackperiod():
    
    for a in model.schedule.agents:
        #calculate PP ratio
        self.agent.PP
    pass


def env_attitude():
    pass

def change_ids(self):
    #for x in range(5):
    #print("i is: ",i)
    #self.unique_id = test_agents_df.loc[x][0]
    return self.unique_id

#************/*****************/*******************/***************
    

#define the agents
#is this the right way?    
# =============================================================================
# 
# for i in range(num_agents)
# agent_one = tpb_agent(attitude(i),network(i),pp(i))
# 
# =============================================================================


try_1 = tpb(5)

try_1.step()









    
    
    
    

