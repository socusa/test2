from tkinter import *
import tkinter as tk

root = tk.Tk()

def toHex(number):
    digits = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']

    firstdigit = digits[number//16]
    seconddigit = digits[number%16]

    return(str(firstdigit) + "" + str(seconddigit))

def hexvalue(r,g,b):
    return("#" + toHex(r) + toHex(g) + toHex(b))

def drawcircle(c,r,g,b):
    red = int(r.get())
    green = int(g.get())
    blue = int(b.get())

    c.create_oval(0,0,100,100,fill=hexvalue(red,green,blue))

redlabel = Label(root,text="Red")
red = Entry(root)
red.insert(0,"200")
greenlabel = Label(root,text="Green")
green = Entry(root)
green.insert(0,"0")
bluelabel = Label(root,text="Blue")
blue = Entry(root)
blue.insert(0,"200")
canvas = Canvas(root,width=100,height=100)
draw = Button(root,text="Draw",command=lambda c=canvas,r=red,g=green,b=blue: drawcircle(c,r,g,b))

redlabel.grid(row=0,column=0)
red.grid(row=0,column=1)
greenlabel.grid(row=1,column=0)
green.grid(row=1,column=1)
bluelabel.grid(row=2,column=0)
blue.grid(row=2,column=1)
draw.grid(row=3,column=0)
canvas.grid(row=4,column=0,columnspan=2)

print(toHex(200))

root.mainloop()