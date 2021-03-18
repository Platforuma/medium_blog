from tkinter import *


root = Tk()
root.title("File Handling")
root.geometry("500x300")

def open_file():
    global text1
    text1.set("")
    if entry_window.get():
        file = open(entry_window.get(),'r') 
        for each in file:
            text1.set(each)

def create_file():
    global text1
    text1.set("")
    if entry_window.get():
        f = open(entry_window.get(), "x")
        text1.set("Create File Successfully")


def append_text():
    global text2
    text1.set("")
    if entry_window.get():
        file = open(entry_window.get(),'r') 
        for each in file:
            text1.set(each)
        file3=open(entry_window.get(),"a")
        #c=input("Enter string to append: \n")
        if entry_window3.get(): 
            #file3.write("\n")
            file3.write(entry_window3.get())
            file3.close()
            text1.set("Append Successfully")



text = StringVar()
text1 = StringVar()
text2 = StringVar()
entry_window = Entry(root,justify=CENTER, width=40, borderwidth=4, textvariable=text)
entry_window.place(x=120,y=40)

btn_check = Button(root,text="Open File", command=open_file)
btn_check.place(x=210,y=80)

entry_window2 = Entry(root,justify=CENTER, width=40,borderwidth=4, textvariable=text1)
entry_window2.place(x=120,y=120, height=50)

label = Label(root,text="Enter text for apeend:")
label.place(x=120,y=175)
entry_window3 = Entry(root,justify=CENTER, width=40, borderwidth=4, textvariable=text2)
entry_window3.place(x=120,y=200)

btn_check1 = Button(root,text="Create File", command=create_file)
btn_check1.place(x=80,y=240)

btn_check2 = Button(root,text="Append Text", command=append_text)
btn_check2.place(x=210,y=240)

btn_check3 = Button(root,text="Close File", command=root.destroy)
btn_check3.place(x=350,y=240)

root.mainloop()
