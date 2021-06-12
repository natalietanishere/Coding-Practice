import tkinter as tk
from tkinter import messagebox
def squareroot():
  sqrt = float(num_input.get()) ** .5
  messagebox.showinfo("square root", sqrt)
def square():
  sq = float(num_input.get()) ** 2
  messagebox.showinfo("square", sq)
main = tk.Tk()
main.title("square and square root calculator")
main.geometry("500x500")
square_button = tk.Button(text="square",command=square)
squareroot_button = tk.Button(text="square root",command=squareroot)
num_input = tk.Entry(main)
#Entry is a single line input
square_button.pack()
squareroot_button.pack()
num_input.pack()
main.mainloop()





