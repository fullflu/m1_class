#coding:utf-8

#copyright :@fullflu

import numpy as np
from math import *
import matplotlib.pyplot as plt

#l1 and l3 are the answers (both two-dimensional arrays) of the quastion


def dy(y,x):
    #an equation to solve
    return y+exp(-x)

def g(x):
    #solve the equation analytically
    return 1.5*exp(x) -0.5*exp(-x)

def fy(y,x,d):
    """
    Euler method
    y_{k+1} = y_k + d*dy/dx
    """
    return y + d*(dy(y,x))


def fz(y,x,d):
    """
    Runge-Kutta method
    y_{k+1} = y_k + 1/6 * (k1 + k2+ k3 + k4)
    """
    
    k1=dy(y,x)
    k2=dy(y+0.5*k1*d,x+0.5*d)
    k3=dy(y+0.5*k2*d,x+0.5*d)
    k4=dy(y+k3*d,x+d)
    
    return (y+d*(k1+2*k2+2*k3+k4)/6)


split=16#number of delta x
delta=0.2
#好きな数に変えてください．ただし，(split-1)*delta=3になるように．delta<1が望ましい


l1=np.empty((split,3))
l3=np.empty((split,3))

def getlist():
    for i in xrange(split):
        
        x0=0#previous x
        x1=0#now x
        
        y0=1#y0,y1:Euler
        y2=1#y2,y3:Runge-Kutta
        
        ll1=np.empty(3)
        ll3=np.empty(3)
        
        h = delta*(i)
        d = 10**(-4 + h) #split range
        
        
        while(x1<1):
            
            x1+=d
            #y1 = y0 + d*(y0 + exp(-x1))
            y1 = fy(y0,x1,d)
            y3 = fz(y2,x1,d)
            
            if x0<=0.2 and 0.2<=x1:
                ll1[0]=log10((y0+(y1-y0)*(0.2-x0)/(x1-x0)-g(0.2))**2)
                ll3[0]=log10((y2+(y3-y2)*(0.2-x0)/(x1-x0)-g(0.2))**2)
                
                
            if x0<=0.5 and 0.5<=x1:
                ll1[1]=log10((y0+(y1-y0)*(0.5-x0)/(x1-x0)-g(0.5))**2)
                ll3[1]=log10((y2+(y3-y2)*(0.5-x0)/(x1-x0)-g(0.5))**2)
                
            if x0<=0.8 and 0.8<=x1:
                ll1[2]=log10((y0+(y1-y0)*(0.8-x0)/(x1-x0)-g(0.8))**2)
                ll3[2]=log10((y2+(y3-y2)*(0.8-x0)/(x1-x0)-g(0.8))**2)
                
                
            y0=y1
            y2=y3
            x0=x1
            
            #----end while loop----
            
        l1[i]=ll1.copy()#Euler
        l3[i]=ll3.copy()#runge-kutta
        
