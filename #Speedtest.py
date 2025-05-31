from tkinter import *
import speedtest
from PIL import Image,ImageTk
import threading



def downspeed():
    def task():
        p=speedtest.Speedtest()
        p.get_servers()
        down=str(round(p.download()/10**6,3)) + "Mbps"
        downsp.config(text=down)
    threading.Thread(target=task).start()


def upspeed():
    def task():
        p=speedtest.Speedtest()
        p.get_servers()
        up=str(round(p.upload()/10**6,3)) + "Mbps"
        upsp.config(text=up)
    threading.Thread(target=task).start()


def speedcheck():
    downspeed()
    upspeed()



root= Tk()
root.title("---> Test")
root.configure(bg="#ff5733")
root.geometry("700x400+300+100")
root.resizable(False,False)

Original_image=Image.open("Speed.png")
resized_image = Original_image.resize((300, 300))
logo=ImageTk.PhotoImage(resized_image)
Label(root,image=logo,bg="#ff5733").place(x=200,y=-90)
Button(root,text="Speed",font=("arial",15,"bold"),fg="Black",bg="#fff4f4",command=speedcheck,relief=RAISED).place(x=310,y=40)


down_image=Image.open("Down.png")
down_resize=down_image.resize((50,50))
downlogo=ImageTk.PhotoImage(down_resize)
Button(root,image=downlogo,bg="#ff5733",command=downspeed,relief=RAISED).place(x=110,y=140)
downsp=Label(root,text="00",font=(NONE,20),bg="#ff5733")
downsp.place(x=120,y=200)




up_image=Image.open("UP 2.png")
up_resize=up_image.resize((50,50))
uplogo=ImageTk.PhotoImage(up_resize)
Button(root,image=uplogo,bg="#ff5733",command=upspeed,relief=RAISED).place(x=490,y=140)
upsp=Label(root,text="00",font=(NONE,20),bg="#ff5733",)
upsp.place(x=500,y=200)





root.mainloop()