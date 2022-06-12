from tkinter import *
import random
import time

root = Tk()
root.geometry("350x350+500+150")
root.title("Number Guessing Game")
root.resizable(width=False, height=False)
root.config(bg="gray")

def OLUSTUR():
    global v
    v = random.randint(1,10)

OLUSTUR()

def TAHMIN():
    if ENTRY1.get() == str(v):
        LABEL2["text"] = "Sonuç : Doğru!"
        OLUSTUR()
    elif ENTRY1.get() > str(v):
        LABEL2["text"] = "Sonuç : Yanlış!"
        LABEL3["text"] = "Daha küçük bir rakam girin"
    elif ENTRY1.get() < str(v):
        LABEL2["text"] = "Sonuç : Yanlış!"
        LABEL3["text"] = "Daha büyük bir rakam girin"

LABEL1 = Label(text="Fazz | Number Guessing", bg="gray", fg="white", font="Arial 14")
LABEL1.place(x=10, y=10)

ENTRY1 = Entry(bg="white", fg="black", font="Arial 14")
ENTRY1.place(x=60, y=50)
ENTRY1.focus()

BUTON1 = Button(text="Tahmin Et", bg="green", fg="white", font="Arial 16", command=TAHMIN)
BUTON1.place(x=110, y=100)

LABEL2 = Label(text="Sonuç : ", bg="gray", fg="magenta", font="Arial 14")
LABEL2.place(x=10, y=170)

LABEL3 = Label(text="İpucu : ", bg="gray", fg="white")
LABEL3.place(x=10, y=200)

root.mainloop()
