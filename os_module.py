from tkinter import*
import os

root = Tk()
root.title("OS Module")
root.geometry("200x200")

def click_on():
    global sc1
    sc1.set("")
    name = os.name
    sc1.set(name)
    

sc1=StringVar('')
label = Label(root, text="This Project used OS Module")
label.pack()

label_1 = Label(root, text="Click on Button for print OS name.")
label_1.pack()

entry=Entry(root,justify = CENTER, textvariable=sc1)
entry.pack()

button = Button(root, text='click', command=click_on)
button.pack()

root.mainloop()
