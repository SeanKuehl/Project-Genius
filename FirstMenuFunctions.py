from tkinter import *
from FrontEnd.UserGUI import *


def StartUpMenu():
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
    button2 = Button(root, text="Settings", height=2, width=20, bg='blue', fg='orange').grid(pady=30)

    button3 = Button(root, text="About", height=2, width=20, bg='blue', fg='orange', command=lambda: About(root)).grid(pady=40)
    button4 = Button(root, text="Close", height=2, width=20, bg='blue', fg='orange', command=lambda: root.destroy()).grid(pady=50)
    # grid_forget





def About(root):
    for item in root.grid_slaves():
        item.grid_forget()

    AboutMenu()
    #this works!





def GeniusMenu():
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
    T = root.Text(root, height=2, width=30).grid(padx=250, pady=40)
    T.insert(root.END, "Enter what you wish to ask Genius here.").grid(padx=250,pady=40)
    button1 = Button(root, text="Transcript", height=2, width=20, bg='blue', fg='orange').grid(padx=250, pady=40)
    button2 = Button(root, text="Settings", height=2, width=20, bg='blue', fg='orange').grid(pady=30)

    button3 = Button(root, text="About", height=2, width=20, bg='blue', fg='orange').grid(pady=40)
    button4 = Button(root, text="Back", height=2, width=20, bg='blue', fg='orange', command=StartUpMenu()).grid(
        pady=50)
    # grid_forget


#def callback():
   # print "click!"

#b = Button(master, text="OK", command=callback)
#b = Button(root, text="Delete me", command=lambda: b.pack_forget())
#use pack_forget to get rid of a button if pack was used to add it to the window


def AboutMenu():
    # this works!
    myLabel = Label(root, text="no buttons, only info on this tab", height=5, bg='dark blue', fg='orange',
                    font=("courier,44")).grid(padx=250)  # label, not on screen

    # this is one method of putting things on the screen
    # puts it on screen in the first available place
    # defaults to "top"
    # Label(master, text="First").grid(row=0)

    # there is row, column. padx is how much horizontal padding
    # grid_remove()
    # fg is text color, bg is box
    button1 = Button(root, text="Genius", height=2, width=20, bg='blue', fg='orange').grid(padx=250, pady=40)
    button2 = Button(root, text="Settings", height=2, width=20, bg='blue', fg='orange').grid(pady=30)

    button3 = Button(root, text="About", height=2, width=20, bg='blue', fg='orange').grid(pady=40)
    button4 = Button(root, text="Close", height=2, width=20, bg='blue', fg='orange', command=root.destroy()).grid(pady=50)
    # grid_forget



