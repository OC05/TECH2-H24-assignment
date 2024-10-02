# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:10:54 2024

@author: olech
"""
# Method 1 using for loops
import math

num_list = [1,2,3,4,5]

def std_loops(x):
    sum_x = 0
    N = 0
    
    for i in num_list:
        N +=1
    
    #computing the mean
        
    for i in range(N):
        sum_x = sum_x + x[i]
        mean_x = sum_x/N
        
        
    sum_x2 = 0
    #computing the mean of squares
    
    for i in range(N):
        sum_x2 = sum_x2 + x[i]**2
        mean_x2 = sum_x2/N
        
            
    #computing the variance
    
    variance = mean_x2 - (mean_x**2)
    
    
    #compute std
    
    std = math.sqrt(variance)
    
    return std


# Method 2

def std_buildtin(x):
    N = len(x)
    
    #compute sum and mean
    
    mean_y = sum(x)/N
    
    #compute mean of squares
    
    mean_y2 = sum(i**2 for i in x)/N
    
    
    #Compute the variance
    
    variance_y = mean_y2 - (mean_y **2)
    
    #compute the standard deviation
    
    std_y = math.sqrt(variance_y)

    return std_y

# Method 3

import numpy

def std_numpy(x):
    return numpy.std(x)

print(std_loops(num_list))













   