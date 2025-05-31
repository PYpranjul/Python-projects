from tkinter import *
import tkinter as tk
from tkinter import ttk,filedialog
from pygame import mixer
import os


root=Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#286237")
root.resizable(False,False)

mixer.init()
def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name=playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(music_name)
    mixer.music.play()

#ICON
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)
top=PhotoImage(file="top.png")
Label(root,image=top,bg="#286237").pack()
#LOGO
logo=PhotoImage(file="logo.png")
Label(root,image=logo,bg="#286237").place(x=65,y=110)
#Play button
play_button=PhotoImage(file="play.png")
Button(root,image=play_button,bg="#286237",command=play_song).place(x=110,y=370)
#pause button
pause=PhotoImage(file="pause.png")
Button(root,image=pause,bg="#286237",command=mixer.music.stop).place(x=30,y=500)
#resume button
resume=PhotoImage(file="resume.png")
Button(root,image=resume,bg="#286237",command=mixer.music.unpause).place(x=130,y=500)
#stop button
stop=PhotoImage(file="stop.png")
Button(root,image=stop,bg="#286237",command=mixer.music.stop).place(x=230,y=500)
#Music
menu=PhotoImage(file="menu.png")
Label(root,image=menu,bg="#286237").pack(padx=10,pady=50,side=RIGHT)
music_frame=Frame(root,bd=20,relief=RIDGE,bg="#286237")
music_frame.place(x=330,y=350,width=560,height=250)
Button(root,text="Open Folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#286237",command=open_folder).place(x=330,y=300)
scroll=Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10,"bold"),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)






root.mainloop()

