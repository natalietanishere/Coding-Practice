import tkinter as tk
from tkinter import *

hey = tk.Tk()
hey.title("Hello")
hey.geometry("500x500")


#class initializes frame
class mainFrame():
    def __init__(self, master=None):
        frame.__init__(self, master)
        self.master = master

wiggy = tk.Canvas(bg="blue",height=300,width=300)

#Picture using the canvas widget
cute_Panda = PhotoImage("https://th.bing.com/th/id/OIP.XqGVlyR6eRZyfpq5TLep9wHaKQ?w=116&h=180&c=7&o=5&dpr=2&pid=1.7")
image = wiggy.create_image(50,50,anchor=NE,image=cute_Panda)
wiggy.pack()

#Exit button function
def clickExitButton(self):
    exit()
#exit button
exitButton = tk.Button(
    hey, text="Exit", background="red", command=exit)
exitButton.place(x=11,y=9)  
#places button at (11,9) on the computer
exitButton.pack()
hey.mainloop()
