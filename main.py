
from tkinter import *


r = Tk()
r.title('轮盘抽奖')
r.wm_minsize(300,400)
n1 = Button(r,text="蓝牙耳机",bg = 'red')
n1.place(x=20,y=20,width=70,height=70)
n2 = Button(r,text="phone",bg = 'white')
n2.place(x=110,y=20,width=70,height=70)
n3 = Button(r,text="lenovo",bg = 'white')
n3.place(x=200,y=20,width=70,height=70)

n4 = Button(r,text="Tesla",bg = 'white')
n4.place(x=20,y=110,width=70,height=70)
n6 = Button(r,text="Chair",bg = 'white')
n6.place(x=200,y=110,width=70,height=70)
n7 = Button(r,text="1",bg = 'white')
n7.place(x=20,y=200,width=70,height=70)
n8 = Button(r,text="2",bg = 'white')
n8.place(x=110,y=200,width=70,height=70)
n9 = Button(r,text="3",bg = 'white')
n9.place(x=200,y=200,width=70,height=70)
ns = Button(r,text="开始")
ns.place(x=70,y=300,width=60,height=40)
ne = Button(r,text="结束")
ne.place(x=160,y=300,width=60,height=40)
if __name__ == '__main__':
    r.mainloop()