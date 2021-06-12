import tkinter as tk
main = tk.Tk()
main.title('Test')
button = tk.Button(text='stop', command=main.destroy)
#stops application once clicked
button.pack() #optional
main.mainloop()
