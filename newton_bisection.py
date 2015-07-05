#coding:utf-8

#copyright :@fullflu

from math import *
import matplotlib.pyplot as plt

def df1(x):
    #f'(x) of 1
    return 16*x -6

def df2(x):
    #f'(x) of 2
    return 2*x + sin(x)

def f1(x):
    #f(x) of 1
    return 8*(x**2) -6*x -4

def f2(x):
    #f(x) of 2
    return x**2 - cos(x)

tol=1e-10#1e-8とかでもいいと思う
max_iter=5000

#Newton method : q is the number of question
def newton(q):
    #now use the same initial values in two questions, but the initial value can be changed
    if q==1:
        f=f1
        df=df1
        ini_1 = -2# -1以下
        ini_2 = 2# 2以上
    else:
        f=f2
        df=df2
        ini_1 = -2 #-1以下
        ini_2 = 2 #1以上
    i=0
    xa=ini_1
    la=[]
    while(1):
        i+=1
        x = xa - 1.0*f(xa)/df(xa)
        la.append(x)
        if((x-xa)**2<tol):
            break
        if i>max_iter:
            print("no convergence")
            break
        xa=x
    #use the same algorithm for different initial value, sorry to be lengthy...
    i=0
    xb=ini_2
    lb=[]
    while(1):
        i+=1
        x = xb - 1.0*f(xb)/df(xb)
        lb.append(x)
        
        if((x-xb)**2<tol):
            break
        
        if i>max_iter:
            print("no convergence")
            break
        xb=x
    #we use only la and lb, but to maintain the consistency return 4 items
    return [la,ini_1,lb,ini_2]


#Bisection method
def binary(q):
    #use the same initial values in two questions, but the initial value can be changed
    if q==1:
        f=f1
        xa_low = -2#-1以下
        xa_up = 0#-1/3以上1以下
        xb_low = 0#-1/3以上1以下
        xb_up = 2#2以上
    else:
        f=f2
        xa_low = -2#-1以下
        xa_up = 0#-Π/6以上Π/6以下
        xb_low = 0#-Π/6以上Π/6以下
        xb_up = 2#1以上
    #iteration number
    i=0
    la=[]
    while(1):
        i+=1
        #use the mean of lower_bound and upper_bound as next xm
        xm = 1.0*(xa_low+xa_up)/2
        la.append(xm)
        #change one of the bounds by XOR
        if( f(xm)*f(xa_low) >= 0):
            temp = xa_low
            xa_low = xm
        else:
            temp = xa_up
            xa_up = xm
            
        if((xm-temp)**2<tol):
            break
        if i>max_iter:
            print("no convergence")
            break
    #use the same algorithm for different initial value, sorry to be lengthy...
    i=0
    lb=[]
    while(1):
        i+=1
        xm = 1.0*(xb_low+xb_up)/2
        lb.append(xm)
        if( f(xm)*f(xb_low) >= 0):
            temp = xb_low
            xb_low = xm
        else:
            temp = xb_up
            xb_up = xm
            
        if((xm-temp)**2<tol):
            break
        if i>max_iter:
            print("no convergence")
            break   
    #we use only la and lb, but to maintain the consistency return 4 items
    return [la,1,lb,1]
    
"""
answer list is below
newton(1)[0]
newton(1)[2]
newton(2)[0]
newton(2)[2]
binary(1)[0]
binary(1)[2]
binary(2)[0]
binary(2)[2]
"""
