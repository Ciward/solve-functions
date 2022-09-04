from tkinter import *
import tkinter
import tkinter.messagebox
import math
def sin(x):
    y=math.sin(x)
    return y
def cos(x):
    y=math.cos(x)
    return y
def lg(x):    
    y=math.log10(x)
    return y
def ln(x):    
    y=math.log(x)
    return y
def logx(base,x):
    y=math.log(x)/math.log(base)
    return y
def kf(x):    
    y=math.sqrt(x)
    return y

class Functions(object):
    def __init__(self,fname):
        self.fname=fname
        self.fname1='f(x)= '+self.fname
        self.L1=[i*0.1 for i in range(-1000,1000)]
        self.L2=[]
        
        self.l=[]
    def pointxy(self):
        e=math.e
        
        for x in self.L1:    
            try:
                y=eval(self.fname)
                if type(y)!=int and type(y)!=float:
                    self.l.append(x)
            except:
                self.l.append(x)
            #print(type(y))
            
        for self.e in self.l:
            self.L1.remove(self.e)
        if self.L1==[]:
            tkinter.messagebox.showerror("错误提示",'请输入正确的格式！！！')
        
    def f(self,x):
        e=math.e
        return eval(self.fname)


class MY_GUI(Tk):
    def __init__(self):
        super(MY_GUI, self).__init__()        
    #设置窗口
        self.title("函数求零点程序")           #窗口名
        self.geometry('400x100+700+20')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        #self.geometry('1068x681+10+10')
        #self["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高


        self.log_label = Label(self, text="f(x)=")
        self.log_label.grid(row=3, column=0)
        self.text = Entry(self)  # 日志框
        self.text.grid(row=3,column = 1, sticky = tkinter.E)
        self.log_label1 = Label(self, text="=0")
        self.log_label1.grid(row=3, column=2)
        self.buttonB = Button(self, text="开始计算！", bg="red", width=10,command=self.convert)  # 调用内部方法  加()为直接调用
        self.buttonB.grid(row=3, column=3)
        self.buttonabout = Button(self, text="关于", width=10,command=self.about).grid(row=3, column=4)  # 调用内部方法  加()为直接调用
       
        

    def convert(self):
        name = self.text.get()
        #try:
        A=Functions(name)
        A.pointxy()
        l=[]
        g=[]
        #以下为主程序   
        for a in A.L1:
            #print(a)
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
            #print(c)
            if A.f(c)==0:
                g.append(c)
            else:    
                while b1-a1>0.0001:
                    if A.f(a1)*A.f(c)<0:
                        b1=c
                        c=(a1+b1)/2
                    elif A.f(b1)*A.f(c)<0:
                        a1=c
                        c=(a1+b1)/2
            g1=(a1+b1)/2
            g2=round(g1,3)
            g.append(g2)        
            n1+=2
            n2+=2
        g=list(set(g))
        string=" ，零点为：  "+str(g)
        if g==[]:
            tkinter.messagebox.showinfo(A.fname1,'无解@_@')
        else:        
            tkinter.messagebox.showinfo(A.fname1,A.fname1+string)
        #except:
            #tkinter.messagebox.showerror("错误提示",'请输入正确的格式！！！')
        
    def about(self):
        tkinter.messagebox.showinfo("关于本软件",'开发者：曦微(QQ2273805191)'+
                                    '\n为方便高中学子攻克数学难题，'+
                                    '\n开发者不辞辛苦，不舍昼夜，'+
                                    '\n牺牲宝贵的学习时间完成此项目，'+
                                    '\n请尊重开发者的劳动成果，侵权必究！！'+
                                    '\n偶尔存在误差请谅解')


        
mywindow = MY_GUI()
# 设置根窗口默认属性
#time.sleep(1)
#mywindow.about()
mywindow.mainloop()
