#2/5/2024
#This program converts C to F and F to C

from tkinter import *
frame = Tk() #creating the application main window
c = Canvas(frame, bg="pink", height="200")

frame.geometry("400x250")
cels = Label(frame, text = "C").place(x = 30, y = 50)
box1 = Entry(frame).place(x = 80, y = 50)

far = Label(frame, text = "F").place(x = 30, y = 90)
box2 = Entry(frame).place(x = 80, y = 90)


def f_formula(f):
      return ((f-32)/2)

def convertButton():
      f = (box2.get())
      c = f_formula(f)
      c.config(text = f)
      
convert = Button(frame, text = "Convert", command=convertButton).place(x = 120, y = 150)

 

c.pack()
frame.mainloop()