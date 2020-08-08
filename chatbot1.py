#importing libraries 
from tkinter import *
import random as rd
from time import time, sleep

#Creating a window 
root=Tk()
root.title('Quote bot')
root.geometry('300x400')
root.resizable(False,False)

    
#send function
def sendval():
    msg1=msgWindow.get("1.0",END)
    msgWindow.delete('0.0',END)
    chatWindow.insert(END, "You : " + msg1.capitalize() + '\n')
    ques=["Hi\n","Hello\n","How are you?\n","How do you do?\n","Who are you?\n","What is your name?\n","What do you do?\n","Tell me a quote\n","Quote for the day\n",
          "Do you like me?\n","Will you marry me?\n","I love you\n","Bye\n","Aloha\n","Goodbye\n"]
    end=["Bye , have a great day!","See you soon","Adios Amigo"]
    tmq=[ "The purpose of our lives is to be happy.","Many of life’s failures are people who did not realize how close they were to success when they gave up.",
          "Your time is limited, so don’t waste it living someone else’s life. Don’t be trapped by dogma – which is living with the results of other people’s thinking.",
          "If you want to live a happy life, tie it to a goal, not to people or things.",
          "The whole secret of a successful life is to find out what is one’s destiny to do, and then do it.","Turn your wounds into wisdom.",
          "Do all the good you can, for all the people you can, in all the ways you can, as long as you can","I like criticism. It makes you strong.",
          "Live for each second without hesitation.", " My mama always said, life is like a box of chocolates. You never know what you’re gonna get",
          "Because of your smile, you make life more beautiful.","Don’t cry because it’s over, smile because it happened.",
          "A smile is the happiness you’ll find right under your nose.","I eat every two hours. I sleep for eight hours. I have lots of water. I pray to keep calm. Most importantly, I have a smile on my face.",
          "Use your smile to change the world; don’t let the world change your smile."]
    iaq=["Your question is inappropriate ","I am not supposed to answer these kinda questions"]
    hru=["I'm fine!","I'm doing great!!!"]
    hi=["Hi", "Hello", "Hello too"]
    wru=["I'm a chatbot. My name is JARVIS. I'm here to help you out with my quotes ;)"]
    error=["Sorry, I can't understand what you asked for?","Sorry I don't know :(" ,"Sorry! Content not found!"]
    if msg1 == ques[0] or msg1==ques[1]:
        chatWindow.insert(END,"JARVIS :" + rd.choice(hi) +'\n\n')
    elif msg1 == ques[2] or msg1==ques[3]:
        chatWindow.insert(END,"JARVIS :" + rd.choice(hru) +'\n\n')
    elif msg1  == ques[4] or msg1==ques[5] or msg1==ques[6]:
        chatWindow.insert(END,"JARVIS :" + wru +'\n\n')
    elif msg1  == ques[7] or msg1==ques[8]:
        chatWindow.insert(END,"JARVIS :" + rd.choice(tmq) +'\n\n')
    elif msg1  == ques[9] or msg1==ques[10] or msg1==ques[11]:
        chatWindow.insert(END,"JARVIS :" + rd.choice(iaq) +'\n\n')
    elif msg1  == ques[12] or msg1==ques[13] or msg1==ques[14]:
        chatWindow.insert(END,"JARVIS :" + rd.choice(end) +'\n\n')
        chatWindow.after(1500,clearChat)
    elif msg1 == ' ' or msg1 == '' or msg1 not in ques:
        chatWindow.insert(END,"JARVIS :" + rd.choice(error) +'\n\n')

    
#Clear chat
def clearChat():
    msgWindow.delete('0.0',END)
    chatWindow.delete('0.0',END)
    
#Details
def details():
    clearChat()
    chatWindow.insert(END,"This is a chatbot for PUBG Mobile created by Ajay \n" 
                      + "Please click clear to proceed further ")


#configuring menu bar and adding sub menus
mainMenu=Menu(root)
fileMenu=Menu(root)
fileMenu.add_command(label='New..',command=clearChat)
fileMenu.add_command(label='Clear chat',command=clearChat)
mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_command(label="Help",command=details)
root.config(menu=mainMenu)

#Chat area
chatWindow=Text(root,bd=1,bg='white',width=50,height=8)
chatWindow.place(x=6,y=6,height=295,width=285)

#Text area
msgWindow=Text(root,bg='white',width=200,height=3,borderwidth=5)
msgWindow.place(x=84,y=305,height=72,width=205)

#Send Button and Clear button
button1=Button(root,text="Send",bg='light green',activebackground='dark green',width=12,height=5,command=sendval)
button1.place(x=6,y=305,height=30,width=65)
button2=Button(root,text="Clear",bg='light green',activebackground='dark green',width=12,height=5,command=clearChat)
button2.place(x=6,y=340,height=30,width=65)

root.mainloop()
    
