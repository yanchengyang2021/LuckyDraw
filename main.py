import threading
import time
from tkinter import *

from PIL import ImageTk

r = Tk()
r.title('轮盘抽奖')
r.wm_minsize(300, 400)

# 背景图片
# photo = PhotoImage(file=r"./images/train1.png")
# 调整图片尺寸适应按钮大小
# photoimage = photo.subsample(3, 3)
photo1 = ImageTk.PhotoImage(file=r"./images/train1.png")
photo2 = ImageTk.PhotoImage(file=r"./images/train2.png")
photo3 = ImageTk.PhotoImage(file=r"./images/train3.png")
photo4 = ImageTk.PhotoImage(file=r"./images/train4.png")
photo5 = ImageTk.PhotoImage(file=r"./images/train5.png")
photo6 = ImageTk.PhotoImage(file=r"./images/train6.png")
photo7 = ImageTk.PhotoImage(file=r"./images/train7.png")
photo8 = ImageTk.PhotoImage(file=r"./images/train8.png")

n1 = Button(r, text="1", bg='red', image=photo1)
n1.place(x=20, y=20, width=70, height=70)
n2 = Button(r, text="2", bg='white', image=photo2)
n2.place(x=110, y=20, width=70, height=70)
n3 = Button(r, text="3", bg='white', image=photo3)
n3.place(x=200, y=20, width=70, height=70)

n4 = Button(r, text="4", bg='white', image=photo4)
n4.place(x=20, y=110, width=70, height=70)
n6 = Button(r, text="5", bg='white', image=photo5)
n6.place(x=200, y=110, width=70, height=70)
n7 = Button(r, text="6", bg='white', image=photo6)
n7.place(x=20, y=200, width=70, height=70)
n8 = Button(r, text="7", bg='white', image=photo7)
n8.place(x=110, y=200, width=70, height=70)
n9 = Button(r, text="8", bg='white', image=photo8)
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
