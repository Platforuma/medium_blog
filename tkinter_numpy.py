from tkinter import*
import numpy as np

root = Tk()
root.title("Numpy Module")
root.geometry("700x400")




def find():
    global sc1 , sc2
    sc1.set("")
    sc2.set("")
    if entry.get():
        if entry_1.get():
            if entry_3.get():
                r = int(entry.get())
                c = int(entry_1.get())
                #n = list(map(int, input().split())) 
                n = (entry_3.get().split())
                matrix = np.array(n).reshape(r, c) 
                a = matrix.size
                b = matrix.shape
                sc1.set(a)
                sc2.set(b)
                
                

sc1=StringVar('')
sc2=StringVar('')
label = Label(root,text="Enter the number of row",font=('arial',20),fg="green")
label.place(x=40,y=70)

entry = Entry(root,justify=CENTER)
entry.place(x=350, y=80)

label_1 = Label(root,text="Enter the number of col",font=('arial',20),fg="green")
label_1.place(x=40,y=130)

entry_1 = Entry(root, justify=CENTER)
entry_1.place(x=350, y=142)

label_3 = Label(root,text="Enter the entries in a single line (separated by space):",font=('arial',20),fg="green")
label_3.place(x=40,y=180)

entry_3 = Entry(root,justify=CENTER,width=40)
entry_3.place(x=400, y=220)

label_2 = Label(root,text="The size of matrix is :",font=('arial',20),fg="green")
label_2.place(x=30,y=250)

entry_2 = Entry(root,justify=CENTER,textvariable=sc1)
entry_2.place(x=330, y=260,height=25)

label_4 = Label(root,text="The shape of matrix in row and col :",font=('arial',20),fg="green")
label_4.place(x=30,y=300)

entry_4 = Entry(root,justify=CENTER,textvariable=sc2)
entry_4.place(x=470, y=310,height=25)

button = Button(root,width=10, justify=CENTER ,text="click",command=find)
button.place(x=250, y=360)





root.mainloop()

