import tkinter as tk
from tkinter import simpledialog
main = tk.Tk()
main.title('hello')
main.withdraw()

usr = simpledialog.askstring(title='test', prompt="What is your name?")
#simpledialog comes with ok and cancel buttons, unlike labels and buttons
#asks input
print("Hello,", usr)
