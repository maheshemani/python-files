# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:47:05 2020

@author: mahesh.emani
"""
import math
import numpy as np

def activate(inputs,weights):
    h=0
    for i,w in zip(inputs,weights):
        h+=i*w
    spike = 1/(1+math.exp(-h))
    return spike



if __name__ == "__main__":
    inputs = [0.1,0.2,0.3]
    weights = [0.1,0.2,0.3]
    print(activate(inputs,weights))
