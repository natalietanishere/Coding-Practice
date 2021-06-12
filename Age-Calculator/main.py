import tkinter as tk
from tkinter import * #* imports all
from datetime import date
main = tk.Tk()
main.title("age")
main.geometry("500x500")

name_value = StringVar() #entry asks for str
year_value = StringVar()
month_value = StringVar()
day_value = StringVar()

#in repl.it, entries have to have grid on seperate line
name_entry = Entry(main,textvariable=name_value)
name_entry.grid(row=1,column=1)
#entry that asks for str as input
year_entry = Entry(main,textvariable=year_value)
year_entry.grid(row=2,column=1)

month_entry = Entry(main,textvariable=month_value)
month_entry.grid(row=3,column=1)

day_entry = Entry(main,textvariable=day_value)
day_entry.grid(row=4,column=1)

Label(text="name").grid(row=1)
Label(text="year").grid(row=2)
Label(text="month").grid(row=3)
Label(text="day").grid(row=4)

def calculateAge():
    # storing today's date in "today" variable
    today = date.today()
    # getting birthdate using .get() method
    birthDate = date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    # calculating age by subtracting birthdate from today's date
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    # creating a Label widget to show the calculated age using
    # grid method
    Label(text=f"{name_value.get()} your age is {age}").grid(row=6, column=1)
  #f(format) rounds the age

age_button = Button(text="Calculate age",command=calculateAge).grid(row=5,column=1)

main.mainloop()


  


