from tkinter import *
from LoadLibrary import returnLists, CheckLists, returnNumOfEntries
import tkinter.scrolledtext as scrolledtext
from AppendLibrary import Append


#tkinter tutorial: https://youtu.be/YXPyB4XeYLA
#every new menu must delete all of the elements from the last one!


root = Tk() #create window
root.geometry("800x600")
root.configure(background='dark blue')
temporaryInt = 0
temporaryString = ""
transcriptList = ['Ask Genius any one sentence question, recieve the wisdom you seek.', ' ']

def Transcript():
    counter = 0

    try:
        for item in root.grid_slaves():
            item.grid_forget()
        #if coming from another page, get rid of it
    except:
        pass

    global transcriptList

    transcriptString = ""

    myLabel = Label(root, text="This is the session transcript so you can see what you've asked.", height=5,
                    bg='dark blue', fg='orange',
                    font=("courier,44")).grid(padx=250)  # label, not on screen

    for item in transcriptList:
        if item != ' ':
            if counter % 2 == 0:
                item = "Genius: "+item
            else:
                item = "User: "+item
        transcriptString += item
        counter += 1



    txt = scrolledtext.ScrolledText(root, undo=True, wrap= WORD, height=2, width=40, bg='black', fg='white', font=('consolas', '12'))
    txt.grid(padx=250, pady=40)
    txt.insert(END, transcriptString)







    button2 = Button(root, text="Back", height=2, width=20, bg='blue', fg='orange',
                     command=lambda: GeniusMenu()).grid(
        padx=250, pady=40)










    #https://stackoverflow.com/questions/13832720/how-to-attach-a-scrollbar-to-a-text-widget/13833338
    #use a giant label and a scrollbar to show off the transcript



def StartUpMenu():

    try:
        for item in root.grid_slaves():
            item.grid_forget()
        #if coming from another page, get rid of it
    except:
        pass
    myLabel = Label(root, text="Welcome to Genius, the knowledge library.", height=5, bg='dark blue', fg='orange',
                    font=("courier,44")).grid(padx=250)  # label, not on screen

    # this is one method of putting things on the screen
    # puts it on screen in the first available place
    # defaults to "top"
    # Label(master, text="First").grid(row=0)

    # there is row, column. padx is how much horizontal padding
    # grid_remove()
    # fg is text color, bg is box
    button1 = Button(root, text="Genius", height=2, width=20, bg='blue', fg='orange', command=lambda: GeniusMenu()).grid(padx=250, pady=40)


    button3 = Button(root, text="About", height=2, width=20, bg='blue', fg='orange', command=lambda: AboutMenu(root)).grid(pady=40)


    button4 = Button(root, text="Close", height=2, width=20, bg='blue', fg='orange', command=lambda: root.destroy()).grid(pady=50)
    # grid_forget






    #this works!


def CheckAnswer(T):
    global temporaryInt, temporaryString, transcriptList
    question = temporaryString


    if temporaryInt == 0:
        question = T.get('1.0', END)
        transcriptList.append(question)

        temp = CheckLists(question)



        if temp == 0:

            #that question hasn't been recorded
            #ask user for answer and append it
            T.delete('1.0', END)
            T.insert(END, "No answer was found. Please enter the answer here.")
            transcriptList.append('No answer was found. Please enter the answer here.')
            transcriptList.append(' ')
            temporaryString = question

            temporaryInt = 1

        if temp != 0:

            transcriptList.append(temp)
            transcriptList.append('Ask Genius any one sentence question, recieve the wisdom you seek.')
            transcriptList.append(' ')
            T.delete('1.0', END)
            T.insert(END, temp)

    elif temporaryInt == 1:
        answer = T.get('1.0', END)
        Append(question, answer)

        temporaryInt = 0
        temporaryString = ""
        T.delete('1.0',END)
        T.insert(END, 'Enter what you wish to ask Genius here.')







def GeniusMenu():
    for item in root.grid_slaves():
        item.grid_forget()
    # this works!
    myLabel = Label(root, text="Ask Genius any one sentence question, recieve the wisdom you seek.", height=5, bg='dark blue', fg='orange',
                    font=("courier,44")).grid(padx=250)  # label, not on screen

    # this is one method of putting things on the screen
    # puts it on screen in the first available place
    # defaults to "top"
    # Label(master, text="First").grid(row=0)

    # there is row, column. padx is how much horizontal padding
    # grid_remove()
    # fg is text color, bg is box
    T = Text(root, height=2, width=40, bg='black', fg='white')
    T.grid(padx=250, pady=40)

    T.insert(END, 'Enter what you wish to ask Genius here.')



    button1 = Button(root, text="Ask", height=2, width=20, bg='blue', fg='orange', command=lambda: CheckAnswer(T)).grid(padx=250, pady=40)

    button2 = Button(root, text="Transcript", height=2, width=20, bg='blue', fg='orange',
                     command=lambda: Transcript()).grid(
        padx=250, pady=40)

    button3 = Button(root, text="Close", height=2, width=20, bg='blue', fg='orange', command=lambda: StartUpMenu()).grid(
        padx=250, pady=40)

    #get(startindex [,endindex])
#This method returns a specific character or a range of text.


    #button2 = Button(root, text="Settings", height=2, width=20, bg='blue', fg='orange').grid(pady=30)

    #button3 = Button(root, text="About", height=2, width=20, bg='blue', fg='orange').grid(pady=40)
   #button4 = Button(root, text="Back", height=2, width=20, bg='blue', fg='orange', command=StartUpMenu()).grid(pady=50)
    # grid_forget


#def callback():
   # print "click!"

#b = Button(master, text="OK", command=callback)
#b = Button(root, text="Delete me", command=lambda: b.pack_forget())
#use pack_forget to get rid of a button if pack was used to add it to the window


def AboutMenu(root):
    # this works!

    for item in root.grid_slaves():
        item.grid_forget()


    numOfEntries = str(returnNumOfEntries())    #can only concantenate string into string
    myLabel = Label(root, text="About this application.", height=5, bg='dark blue', fg='orange',
                    font=("courier,44")).grid(padx=250)  # label, not on screen

    mainText = Label(root, text="   The Genius library has "+numOfEntries+" entries and is always growing. This application was made using Python and Tkinter.", height=20, bg='dark blue', fg='orange', font=("courier,44")).grid(padx=250)

    # this is one method of putting things on the screen
    # puts it on screen in the first available place
    # defaults to "top"
    # Label(master, text="First").grid(row=0)

    # there is row, column. padx is how much horizontal padding
    # grid_remove()
    # fg is text color, bg is box

    button1 = Button(root, text="Close", height=2, width=20, bg='blue', fg='orange', command=lambda: StartUpMenu()).grid(pady=50)
    # grid_forget


StartUpMenu()




root.mainloop() #will loop until program ends, creates window
root.destroy()

