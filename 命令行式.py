import math
import tkinter
import tkinter.messagebox
import numpy as np
def log(x):    
    y=math.log(x)
    return y
def logx(base,x):
    y=math.log(x)/math.log(base)
    return y
def KF(x):    
    y=math.sqrt(x)
    return y

class Functions(object):
    def __init__(self):
        self.fname=input('表达式：f(x)=')
        self.fname1='f(x)= '+self.fname
        self.L1=list(np.arange(-100,100,0.1))
        self.L2=[]
        
        self.l=[]
    def pointxy(self):
        
        
        for x in self.L1:    
            try:
                self.y=eval(self.fname)
                
            except:
                self.l.append(x)
        for self.e in self.l:
            self.L1.remove(self.e)
        
    def f(self,x):
        return eval(self.fname)
        

while True:    
    A=Functions()
    A.pointxy()
    l=[]
    g=[]
    print(A.L1)

    #以下为主程序
   
    for a in A.L1:
        b=a+1
        y1=A.f(a)
        y2=A.f(b)
        s=y1*y2
        if s<0:
            l.append(a)
            l.append(b)
        if y1==0:
            g.append(a)
        elif y2==0:
            g.append(b)

    n1=0
    n2=1

    while n1<len(l):
        a1=l[n1]
        b1=l[n2]
        c=(a1+b1)/2
        if A.f(c)==0:
            g.append(c)
        while b1-a1>0.01:
            if A.f(a1)*A.f(c)<0:
                b1=c
                c=(a1+b1)/2
            elif A.f(b1)*A.f(c)<0:
                a1=c
                c=(a1+b1)/2
        g1=(a1+b1)/2
        g2=round(g1,2)
        g.append(g2)        
        n1+=2
        n2+=2
    g=list(set(g))
    string="零点为：  "+str(g)
    if g==[]:
        tkinter.messagebox.showinfo(A.fname1,'无解@_@')
    else:
        tkinter.messagebox.showinfo(A.fname1,string)
    print('\n'*2)
    

