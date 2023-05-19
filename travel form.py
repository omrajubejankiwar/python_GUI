import tkinter
from tkinter import *
from tkinter .ttk import Combobox
root=tkinter.Tk()
root.title("travel form")
root.geometry("600x400")
#heading
heading=tkinter.Label(root,text="sriram travels",bg="orange",font="comicsansms 20 bold",pady="9")
heading.pack(fill="x",pady=10)
#frame
root1=Frame(root)
root1.pack()
def storedata():
    mydata=open("traveldata.txt","a")
    mydata.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),paymentmodevalue.get(),foodvalue.get()}\r")
#labels
name=Label(root1,text="name                 :",font=10,pady=10)
phone=Label(root1,text="phone number     :",font=10,pady=10)
gender=Label(root1,text="gender               : ",font=10,pady=10)
paymentmode=Label(root1,text="paymentmode    :",font=10,pady=10)

name.grid(row=0,column=0)
phone.grid(row=1,column=0)
gender.grid(row=2,column=0)
paymentmode.grid(row=3,column=0)
#variables
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
paymentmodevalue=StringVar()
foodvalue=IntVar()
#entry
nameentry=Entry(root1,textvariable=namevalue,font=11)
phoneentry=Entry(root1,textvariable=phonevalue,font=11)
genderentry=Entry(root1,textvariable=gendervalue,font=11)
paymentmodeentry=Combobox(root1,textvariable=paymentmodevalue,values=["net banking","UPI","debit card","cradit card"],font=8)

nameentry.grid(row=0,column=1)
phoneentry.grid(row=1,column=1)
genderentry.grid(row=2,column=1)
paymentmodeentry.grid(row=3,column=1)
#checkbox
foodservice=Checkbutton(root1,text="would you like to prebook meals ?",font=8,variable=foodvalue)
foodservice.grid(row=5,column=1)
#submitbutton
submit=Button(root,text="sumit data",bg="sky blue",font=15,command=storedata)
submit.pack(pady=30)

root.mainloop()
