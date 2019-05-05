import gym
from gym import spaces
import numpy as np
import random

class Gobang(gym.Env):
    metadata={'render.modes':['human','ai'],
              'video.frame_per_second':2
              }
    def __init__(self):
        self.size=15
        self.board=np.zeros((15,15))
        self.viewer=None
        self.step_count=0
    
    def seed(self,seed=None):
        self.np_random,seed=seeding.np_random(seed)
        return [seed]
    
    def vaild_step(self,x,y):
        if x>=0 and x<self.size and y>=0 and y<self.size:
            if self.board[x][y]==0:
                return x,y
    def set_position(self):
        result=[]
        for i in range(15):
            for j in range(15):
                if self.board[i][j]==0:
                    result.append(1)
                else:
                    result.append(0)
        return result          
    
    def step(self,action):
        action[2]=self.board[action[0]][action[1]]
        self.step_count +=1
        color =action[2]
        win_piont=1000
        normol_point=-10
        draw_point=0
        color=action[2]
        
        
        