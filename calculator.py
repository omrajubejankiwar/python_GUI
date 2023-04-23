import tkinter
from tkinter import *

#title
root=tkinter.Tk()
root.title("calculator")
root.geometry("480x495")

def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)
def btnclear():
    global val
    val=data.get()
    val=val[0:len(val)-1]
    data.set(val)
def btnequals():
    global val
    result=str(eval(val))
    data.set(result)
val=""
data=StringVar()

display=Entry(root,textvariable=data,bd=29,justify="right",bg="sky blue",font=("arial",28))
display.grid(row=0,columnspan=4)

#row 1 buttons
btn7=Button(root,text="7",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick(9))
btn9.grid(row=1,column=2)
btnadd=Button(root,text="+",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick("+"))
btnadd.grid(row=1,column=3)
#row 2 bottons
btn4=Button(root,text="4",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick(6))
btn6.grid(row=2,column=2)
btnsub=Button(root,text="-",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick("-"))
btnsub.grid(row=2,column=3)
#row 3 bottons
btn1=Button(root,text="1",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick(3))
btn3.grid(row=3,column=2)
btnequal=Button(root,text="=",font=("arial",12),bd=13,height=3,width=7,command=btnequals)
btnequal.grid(row=3,column=3)
#row 4 bottons
btnmult=Button(root,text="*",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick("*"))
btnmult.grid(row=4,column=0)
btn0=Button(root,text="0",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick(0))
btn0.grid(row=4,column=1)
btndiv=Button(root,text="%",font=("arial",12),bd=13,height=3,width=7,command=lambda:btnclick("/"))
btndiv.grid(row=4,column=2)
btnc=Button(root,text="C",font=("arial",12),bd=13,height=3,width=7,command=btnclear)
btnc.grid(row=4,column=3)

root.mainloop()
