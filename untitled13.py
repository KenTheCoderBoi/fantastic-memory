from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.geometry("600x600")
root.title("sus among us")

russia=Image.open("russia.png")
vietnam=Image.open("vietnam.png")
china.png=Image.open("china.png")
america=Image.open("download (5).png")

ent=Entry(root)
ent.place(relx=0.5,rely=0.4,anchor=CENTER)
img=Label(root)
img.place(relx=0.5,rely=0.5,anchor=CENTER)
array=["America","Russia","China","Vietnam"]
def search():
    if ent.get()==array.includes():
        img(root,image=ent.get)
    else:
        messagebox.showinfo("nope flag doesnt exist byee")
btn=Button(root,text=Check,command=search)
btn.place(relx=0.5,rely=0.45)
root.mainloop()