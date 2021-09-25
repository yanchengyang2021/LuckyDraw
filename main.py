import threading
import time
from tkinter import *

r = Tk()
r.title('轮盘抽奖')
r.wm_minsize(300, 400)
n1 = Button(r, text="蓝牙耳机", bg='red')
n1.place(x=20, y=20, width=70, height=70)
n2 = Button(r, text="phone", bg='white')
n2.place(x=110, y=20, width=70, height=70)
n3 = Button(r, text="lenovo", bg='white')
n3.place(x=200, y=20, width=70, height=70)

n4 = Button(r, text="Tesla", bg='white')
n4.place(x=20, y=110, width=70, height=70)
n6 = Button(r, text="Chair", bg='white')
n6.place(x=200, y=110, width=70, height=70)
n7 = Button(r, text="1", bg='white')
n7.place(x=20, y=200, width=70, height=70)
n8 = Button(r, text="2", bg='white')
n8.place(x=110, y=200, width=70, height=70)
n9 = Button(r, text="3", bg='white')
n9.place(x=200, y=200, width=70, height=70)

p = [n1, n2, n3, n4, n6, n7, n8, n9]
isloop = False
run = False


def stop():
    global isloop
    global run

    run = False
    isloop = False


def round():
    i = 0
    while 1:
        time.sleep(0.06)
        for j in p:
            j['bg'] = 'white'
        p[i]['bg'] = 'red'
        i += 1
        if i > 7:
            i = 0
        if run == True:
            continue
        else:
            break


def start():
    global isloop
    global run
    t = threading.Thread(target=round)
    t.start()
    isloop = True
    run = True


ns = Button(r, text="开始", command=start)
ns.place(x=70, y=300, width=60, height=40)
ne = Button(r, text="结束", command=stop)
ne.place(x=160, y=300, width=60, height=40)
if __name__ == '__main__':
    r.mainloop()
