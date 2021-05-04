from tkinter import *
from urllib.request import Request, urlopen

root = Tk()
root.title("URLLIB MODULE")
root.geometry("500x250")

def Open_url():
    global text
    text.set("")
    if entry_window.get():
        req = Request(entry_window.get(), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        #print(webpage)
        file = open(entry_window2.get(),"w")
        file.write(str(webpage))
        text.set("Open URL Successfully ...")

text = StringVar()
label = Label(root,text="Enter any URL :")
label.place(x=95, y=10)

entry_window = Entry(root,justify=CENTER, width=50, borderwidth=4)
entry_window.place(x=95,y=30)



label = Label(root,text="Enter file name for save response :")
label.place(x=95, y=60)

entry_window2 = Entry(root,justify=CENTER, width=50, borderwidth=4)
entry_window2.place(x=95, y=80)

label = Label(root,text="Status of Response :")
label.place(x=95, y=110)
entry_window1 = Entry(root,justify=CENTER, width=50, borderwidth=4, textvariable=text)
entry_window1.place(x=95,y=130,height=30)

btn_check = Button(root,text="Open URL", command=Open_url)
btn_check.place(x=220,y=180)
root.mainloop()
