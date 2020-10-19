# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:24:49 2020

@author: mahesh.emani
"""

import numpy as np

class MLP:
    def __init__(self,num_inputs=5,num_hidden=[5,5],num_outputs=5):
        self.num_inputs=num_inputs
        self.num_hidden=num_hidden
        self.num_outputs=num_outputs
        """
        all the parameters indicate the no.of neurons in each layer
        num_hidden is a list. Length of list is the num of hidden layers
        and the elements indicate the no.of neurons in each layer
        """
        neu_per_layer= [self.num_inputs] + self.num_hidden + [self.num_outputs]
        
        #calculate the weights matrices for all the stages
        weights = []
        for i in range(len(neu_per_layer)-1):
            w=np.random.rand(neu_per_layer[i],neu_per_layer[i+1])
            weights.append(w)
        self.weights = weights
        
        #create activation matrix
        a_matrix=[]
        for i in neu_per_layer:
            a=np.zeros(i)
            a_matrix.append(a)
        self.a_matrix=a_matrix
        
        #create derivates matrix
        derivatives = []
        for i in range(len(neu_per_layer)-1):
            d=np.random.rand(neu_per_layer[i],neu_per_layer[i+1])
            derivatives.append(d)
        self.derivatives = derivatives
    
    
        
    def forward_propagation(self,inputs):
        """
        this function uses the input matrix from the user 
        and applies the weights matrix itertively until output layer is obtained
        we do not store the intermediate neuron values
        """
        a_matrix=inputs
        self.a_matrix[0]=inputs
        for i,w in enumerate(self.weights):
            h_matrix=np.dot(a_matrix,w)
            #update the a_matrix with new layer inputs
            a_matrix=self._sigmoid(h_matrix)
            self.a_matrix[i+1]=a_matrix
        return a_matrix
    
    def back_propagation(self,error):
        
    
    def _sigmoid(self,x):
        return 1/(1+np.exp(-x))
    
    
    
if __name__ == "__main__":
    
    #define Multilayer Perceptron
    mlp=MLP()
    
    #create inputs
    inputs = np.random.rand(mlp.num_inputs)
    
    #forward propagation
    outputs = mlp.forward_propagation(inputs)
    
    #print outputs
    print("inputs are :", inputs)
    print("outputs are :", outputs)
    
    
     
            
            
        