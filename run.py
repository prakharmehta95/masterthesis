# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:40:34 2019

@author: iA
"""

#run.py

from model_space import * #imports everything from that python code
import matplotlib.pyplot as plt
import numpy as np
from mesa.batchrunner import BatchRunner
from server import server


fixed_params = {"width": 10,
                "height": 10}
variable_params = {"N": range(10,50,10)}

batch_run = BatchRunner(MoneyModel,variable_parameters = variable_params,
                        fixed_parameters = fixed_params, iterations = 5,
                        max_steps = 100,
                        model_reporters = {"Gini": compute_gini},
                        agent_reporters = {"Wealth": "wealth"},
                        display_progress = True)

batch_run.run_all()

run_data = batch_run.get_model_vars_dataframe()
run_data.head()
run_data_agents = batch_run.get_agent_vars_dataframe()
plt.scatter(run_data.N, run_data.Gini)


server.port = 8521
server.launch()

# =============================================================================
# =============================================================================
# model = MoneyModel(100)
# 
# #for j in range(10):    
# for i in range(1):
#     model.step()
#     #print(a.unique_id)
# 
# 
# agent_wealth = [a.wealth for a in model.schedule.agents] #making a list of the data to make a histogram of it
# print(agent_wealth)
# plt.hist(agent_wealth)
# plt.show()
# 
# 
# =============================================================================

# 
# =============================================================================
#print("The total wealth remains, of course,", sum(agent_wealth))
# =============================================================================
# 
# =============================================================================
# 
# all_wealth = []
# for j in range(100):
#      #run the model 100 times
#     test_model = MoneyModel(10)
#     for i in range(1):
#         test_model.step()
#  
#     for agent in test_model.schedule.agents:
#         all_wealth.append(agent.wealth)
#  
#  #plt.hist(all_wealth)
# plt.hist(all_wealth, bins=range(max(all_wealth)+1))
# print("The total wealth remains, of course,", sum(all_wealth))
# # 
# =============================================================================

# =============================================================================
# 
# model = MoneyModel(50,10,10)
# for i in range(100):
#     model.step()
#  
#     
# gini = model.datacollector.get_model_vars_dataframe()
# #gini.plot()
# 
# 
# agent_wealth = model.datacollector.get_agent_vars_dataframe()
# agent_wealth.head()
# 
# end_wealth = agent_wealth.xs(99,level = "Step")["Wealth"]
# #end_wealth.hist(bins=range(agent_wealth.Wealth.max()+1))
# 
# one_agent_wealth = agent_wealth.xs(14, level="AgentID")
# one_agent_wealth.Wealth.plot()
# # =============================================================================
# =============================================================================
#     
# agent_counts = np.zeros((model.grid.width,model.grid.height))
# for cell in model.grid.coord_iter():
#     cell_content, x, y = cell
#     agent_count = len(cell_content)
#     agent_counts[x][y] = agent_count
# 
# plt.imshow(agent_counts,interpolation = 'nearest')
# plt.colorbar()
# plt.show()
# 
# =============================================================================
