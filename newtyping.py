words = ['mango','orange','hello','banana','indore','hospital','python','java','jamghat','ratlam','cow','yellow','black','computer','blue']



def labelSlider():
    global count, sliderwords,speed
    text = "Welcome to typing Speed Increaser Game"

    if (count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontLabel.configure(text=sliderwords)
    fontLabel.after(150,labelSlider)

def time():
    global timeleft, score,miss, speed, total
    if(timeleft >= 12):
        pass
    else:
        timeLabelCount.configure(fg='red')
    if(timeleft>0):
        timeleft -= 1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
        if(timeleft==0):  
            pass
            #print(letter)############list to all letter matched
        if(timeleft==0):
            speed = speed.join(letter)
            #print(speed)############### all character matched
            #print(len(speed))
            total = ((len(speed)) / 60) 
            #print(total)
            print('Typing Speed is ', math.ceil(total),'letter/sec')


            
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        speedperseclLabel.configure(text='Typing Speed in letter/sec = {}'.format(math.ceil(total)))
        rr = messagebox.askretrycancel('Notification','Play Again Hit Retry Button')
        if(rr==True):
            score = 0
            timeleft = 60
            miss = 0
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)



def startGame(event):
    global score, miss , speed
    if(timeleft == 60):
        time()
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
    if(wordEntry.get() == wordLabel['text']):
        letter.append(wordEntry.get())
        
    
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)
    
####################################

from tkinter import *
import random
from tkinter import messagebox
import math

########################     Root Method
root = Tk()
root.geometry("800x550+400+100")
root.configure(bg="powder blue")
root.title("Typing Speed Increser Game")

#####################       Variable Section

score = 0
timeleft = 60
count = 0
sliderwords = ''
miss = 0
letter = []
speed = ''
total = ''




######################       Lable Method

fontLabel = Label(root, text=" ", font=("airal",25, "italic bold"),
                  bg="powder blue",fg="red",width=40)
fontLabel.place(x=10, y=10)
labelSlider()

random.shuffle(words)

wordLabel = Label(root,text=words[0],font=("airal",40, "italic bold"),bg='powder blue')
wordLabel.place(x=350, y=200)

scoreLabel = Label(root,text="Your Score :",font=("airal",25, "italic bold"),bg="powder blue")
scoreLabel.place(x=10,y=100)


scoreLabelCount = Label(root,text=score,font=("airal",25, "italic bold"),bg="powder blue",fg='blue')
scoreLabelCount.place(x=80,y=180)

timerCount = Label(root,text="Time Left :",font=("airal",25, "italic bold"),bg="powder blue")
timerCount.place(x=600,y=100)

timeLabelCount = Label(root,text=timeleft,font=("airal",25, "italic bold"),bg="powder blue",fg='blue')
timeLabelCount.place(x=680,y=180)

gamePlayDetailLabel = Label(root,text="Type Word and Hit Button",font=("airal",20, "italic bold"),bg="powder blue",fg='violet red')
gamePlayDetailLabel.place(x=180,y=450)

speedperseclLabel = Label(root,font=("airal",35, "italic bold"),bg="powder blue",fg='red')
speedperseclLabel.place(x=85,y=480)



#######################     Entry Method

wordEntry = Entry(root,font=("airal",25, "italic bold"),bd=10,justify="center")
wordEntry.place(x=250,y=300)
wordEntry.focus_set()
################################################################



root.bind('<Return>',startGame)


root.mainloop()
