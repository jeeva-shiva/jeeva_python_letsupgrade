from pytube import YouTube
import os
from tkinter import *

root=Tk()
root.geometry('800x500')
root.title('Youtube Video')

Label_1=Label(root,text="link Here", font=("bold",25))
Label_1.place(x=120,y=30)

mylink=StringVar()
pastelink=Entry(root, width=50, textvariable=mylink)
pastelink.place(x=150, y=900)

def downloadVideo():
    x=str(mylink.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('F:/'):
        os.makedirs('F:/pyt')
    ytvideo.download('F:/') 

Button(root,text="Download Video", width=40, bg='green',fg="white", command=downloadVideo).place(x=200, y=130)

root.mainloop()

