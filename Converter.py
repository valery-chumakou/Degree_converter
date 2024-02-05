#2/5/2024
#This program converts C to F and F to C

from tkinter import *
frame = Tk() #creating the application main window
c = Canvas(frame, bg="pink", height="400", width="500")
frame.geometry("400x250")

frame.resizable(0,0)
cels = Label(frame, text = "C").place(x = 30, y = 50)
box1 = Entry(frame)
box1.place(x = 80, y = 50)
 

far = Label(frame, text = "F").place(x = 30, y = 90)
box2 = Entry(frame)
box2.place(x = 80, y = 90)



def f_formula(f):
      return ((f-32)/2)

def c_formula(c):
      return ((c*9/5+32))

def convertButton():
      f = float(box2.get())
      c = f_formula(f)
      box1.delete(0,END)
      box1.insert(0,str(round(c,2)))
      
       

def convertButton2():
      c = float(box1.get())
      f = c_formula(c)
      box2.delete(0,END)
      box2.insert(0,str(round(f,2)))

convert = Button(frame, text = "Convert", command=convertButton)
convert.place(x = 120, y = 150)
convert2 = Button(frame, text="Convert C to F", command=convertButton2)
convert2.place(x=200, y = 140)
 

c.pack()
frame.mainloop()