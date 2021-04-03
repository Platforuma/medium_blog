from tkinter import *
#from tkinter.ttk import Combobox
#import random
import hashlib

screen = Tk()
screen.title("Password Generator")
screen.geometry('600x400')
screen.configure(background ="bisque")



def gen():
    global sc1, result, c1
    sc1.set("")
    passw=""    
    if c1.get() :
        result = hashlib.sha256(c1.get().encode()) 
        passw = result.hexdigest()
        sc1.set(passw)
    

sc1=StringVar('')
t1=Label(screen,text='Automatic # sha256 Generator',font=('Arial',25),fg='red',background ="bisque")
t1.place(x=60,y=0)
t2=Label(screen,text='SHA256 #code:',font=('Arial',14),background ="bisque")
t2.place(x=145,y=90)

il=Entry(screen,font=('Arial',14),textvariable=sc1)
il.place(x=280,y=90)
t3=Label(screen,text='Type word  ',font=('Arial',14),background ="bisque")
t3.place(x=145,y=120)



c1=Entry(screen,font=('Arial',14),width=10)
c1.place(x=280,y=120)



b=Button(screen,text='Generate',font=('Arial',14),fg='red',background ="white",command=gen)
b.place(x=230,y=195)


###################



screen.mainloop()
