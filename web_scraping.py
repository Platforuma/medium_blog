#           Perform Consumer Research

from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("Web Scraper")
root.geometry("500x400")

def find():
    if entry.get():
        if entry_1.get():
            url = entry.get()
            r = requests.get(url)
            htmlContent = r.content
            soup = BeautifulSoup(htmlContent,"html.parser")
            #print(soup.prettify)
            abc = soup.find().get_text(entry_1.get())
            #print(abc)
            #find_word = soup.find_all(entry_1.get())
            #print(find_word)
            
            file = open(entry_2.get(),"w")
            file.write(abc)


label = Label(root,text="Enter Correct URL",font=('arial',20),fg="black")
label.place(x=138,y=30)

entry = Entry(root, width=45)
entry.place(x=120, y=80)

label_1 = Label(root,text="Find words",font=('arial',20),fg="green")
label_1.place(x=40,y=130)

entry_1 = Entry(root)
entry_1.place(x=200, y=142)

label_2 = Label(root,text="Give name for save file",font=('arial',20),fg="green")
label_2.place(x=30,y=180)

entry_2 = Entry(root)
entry_2.place(x=320, y=190)

button = Button(root,width=10, text="click",command=find)
button.place(x=180, y=240)





root.mainloop()
