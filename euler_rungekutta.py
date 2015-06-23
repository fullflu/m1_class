#coding:utf-8

import numpy as np
from math import *
import matplotlib.pyplot as plt

#l1 and l3 are the answers (both two-dimensional arrays) of the class report

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

l1=np.empty((split,3))
l3=np.empty((split,3))

for i in xrange(split):
    
    x0=0#previous x
    x1=0#now x
    
    y0=1#y0,y1:Euler
    y2=1#y2,y3:Runge-Kutta
    
    ll1=np.empty(3)
    ll3=np.empty(3)
    
    h = 0.2*(i)
    d = 10**(-4 + h) #split range
    
    
    while(x1<1):
        
        x1+=d
        #y1 = y0 + d*(y0 + exp(-x1))
        y1 = fy(y0,x1,d)
        y3 = fz(y2,x1,d)
        
        if x0<=0.2 and 0.2<=x1:
            ll1[0]=(y0+(y1-y0)*(0.2-x0)/(x1-x0)-g(0.2))**2
            ll3[0]=(y2+(y3-y2)*(0.2-x0)/(x1-x0)-g(0.2))**2
            
            
        if x0<=0.5 and 0.5<=x1:
            ll1[1]=(y0+(y1-y0)*(0.5-x0)/(x1-x0)-g(0.5))**2
            ll3[1]=(y2+(y3-y2)*(0.5-x0)/(x1-x0)-g(0.5))**2
            
        if x0<=0.8 and 0.8<=x1:
            ll1[2]=(y0+(y1-y0)*(0.8-x0)/(x1-x0)-g(0.8))**2
            ll3[2]=(y2+(y3-y2)*(0.8-x0)/(x1-x0)-g(0.8))**2
            
            
        y0=y1
        y2=y3
        x0=x1
        
        #----end while loop----
        
    l1[i]=ll1.copy()#Euler
    l3[i]=ll3.copy()#runge-kutta
    
#plot one method in one figure
def plot(mode):
    
    ax_list = [-4+0.2*(i) for i in xrange(split)]
    x_list = [i for i in xrange(split)]
    
    
    if mode==1:
        a=l1
        method="Euler"
        
    else:
        a=l3
        method="Runge-Kutta"
    
    label=[0.2,0.5,0.8]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for i in xrange(3):
        ax.plot(a.T[2-i],label="x={}".format(label[2-i]))
    plt.legend(loc="upper left")
    ax.set_title("{} method approximation".format(method))
    plt.ylim([0,0.4])
    plt.xlim([0,split-1])
    ax.set_xlabel(r"$\log_{10}(\Delta x)$")
    ax.set_xticks(x_list)
    ax.set_xticklabels(ax_list)
    ax.set_ylabel("error")
    
    #plt.show()
    
    #a figure is saved by the following line
    plt.savefig("{}_method.pdf".format(method),format="pdf")#
    
#plot two methods in one figure   
def plo():
    ax_list = [-4+0.2*(i) for i in xrange(split)]
    x_list = [i for i in xrange(split)]
    
    col=["r","g","b"]
    label=[0.2,0.5,0.8]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for i in xrange(3):
        ax.plot(l1.T[2-i],color=col[i],linestyle="dashed",label="x={},Euler".format(label[2-i]))
    for i in xrange(3):
        ax.plot(l3.T[2-i],color=col[i],label="x={},Runge-Kutta".format(label[2-i]))
    plt.legend(loc="upper left")
    ax.set_title("{} and {} approximation".format("Euler","Runge-Kutta"))
    #plt.ylim([0,0.4])
    plt.xlim([0,split-1])
    ax.set_xlabel(r"$\log_{10}(\Delta x)$")
    ax.set_xticks(x_list)
    ax.set_xticklabels(ax_list)
    ax.set_ylabel("error")
    #ax.set_yticks([0,1,2,3])
    
    #plt.show()
    
    #figure is saved by the following line
    plt.savefig("{}.pdf".format("report"),format="pdf")
    
