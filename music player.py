import os
import pygame
from tkinter.filedialog import askdirectory
from tkinter import *
from mutagen.id3 import ID3
root=Tk()
root.minsize(300,300)
listofsongs=[]
realnames=[]
v=StringVar()
songlabel=Label(root,textvariable=v,width=35)
index=0
def updatelabel():
    global index
    v.set(realnames[index])
def directorychooser():
    directory=askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir=os.path.realpath(files) 
            audio=ID3(realdir)
            listofsongs.append(files)
            realnames.append(audio["TIT2"].text[0]) 
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
def nextsong(event):
    global index
    index+=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
def prevsong(event):
    global index
    index-=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
directorychooser()

label=Label(root,text="Music Player")
label.pack()

listbox=Listbox(root)
listbox.pack()

realnames.reverse()
for items in realnames:
    listbox.insert(0,items)
realnames.reverse()

nextbutton=Button(root,text="Next Song")
nextbutton.pack()

previousbutton=Button(root,text="Previous Song")
previousbutton.pack()

stopbutton=Button(root,text="Stop Music")
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()
root.mainloop()
