import tkinter
from tkinter import *
from tkinter import messagebox

#title
root=tkinter.Tk()
root.title("login screen")
root.geometry("400x220")
fr=Frame(root)
fr.pack()``

#label
la1=Label(fr,text="username",font=(14))
la2=Label(fr,text="password",font=(14))
la1.grid(row=0,column=0,padx=5,pady=5)
la2.grid(row=1,column=0,padx=5,pady=5)

username=StringVar()
password=StringVar()

#entry
t1=Entry(fr,textvariable=username,font=(14))
t2=Entry(fr,textvariable=password,font=(14),show='*') #show is used for hide latters entered by user
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)

#enterdata
def enterdata():
    root.destroy()
    sun=input("please entere sun ->")
    name=input("please enter your full name ->")
    cource=input("please enter your cource name ->")
    feedback=input("please enter feedback ->")
    suggestion=input("please enter your suggestion ->")
    mydata=open(sun+".txt","x")
    mydata.write("sun\t\t-{}\n".format(sun))
    mydata.write("Full Name\t-{}\n".format(name))
    mydata.write("Cource Name\t-{}\n".format(cource))
    mydata.write("Feedback\t-{}\n".format(feedback))
    mydata.write("suggestion\t-{}\n".format(suggestion))
    mydata.close()
    mydata=open(sun+".txt","r")
    print(mydata.read())
    mydata.close()
#old data
def olddata():
    root.destroy()
    a=input("please enter SUN number\n")
    mydata=open(a+".txt","r")
    print(mydata.read())
    mydata.close()
#massage
def login():
    if (username.get()=="admin" and password.get()=="admin") :
        b3=Button(root,text="ENTER NEW DATA",command=enterdata,font=(3),bg="light grey")
        b4=Button(root,text="CHECK OLD DATA",command=olddata,font=(3),bg="light grey")
        b3.pack(padx=5,pady=5)
        b4.pack(padx=3,pady=3)
        
    else :
        messagebox.showerror(title="login error",message="username/password is incorrect")
        #shows error
def cancel():
    status=messagebox.askyesno(title="quation",message="do you want to close window")
    #askyesno
    if (status==True):
        root.destroy()
    else:
        messagebox.showwarning(title="warning massage",message="please login again")
        #show warning
#button
b1=Button(fr,text="login",command=login,font=(14),bg="powder blue")
b2=Button(fr,text="cancel",command=cancel,font=(14))
b1.grid(row=2,column=1,sticky=W) #W for right side
b2.grid(row=2,column=1,sticky=E) #E for left side
root.mainloop()

