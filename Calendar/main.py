months=["January","February","March","April","May","September","October","November","December"]
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]  
dates=["1","2","3","4","5","6"
,"7","8","9","10","11","12","13",
"14","15","16","17","18",
"19","20","21","22","23","24","25","26","27","28","29","30","31"]
year=("2020")
choices=("yes","no","Yes","No")

day=input("What day is it?")
while day not in days:
  day=input("Invalid day, what is the day?")
#You are filing your first event.
  
month=input("What month is it?")
while month not in months:
  month=input("Invalid month, what month is it?")
   
date=input("What is the date?")
while date not in dates:
  date=input("Invali date, what is the date?")
   
if day in days and month in months and date in dates:
  print(day,month,date,year)
#After all questions are answered, the full date appears.
  
choice=input("Do you want to enter another event?")
while choice not in choices:
  choice=input("Yes or No?")

while choice=="Yes":
  day=input("What day is it?")
  while day not in days:
   day=input("Invalid day, what is the day?")
#You file another date.
   
   month=input("What month is it?")
  while month not in months:
   month=input("Invalid month, what month is it?")
   
   date=input("What is the date?")
  while date not in dates:
   date=input("Invali date, what is the date?")
  if day in days and month in months and date in dates:
    print(day,month,date,year)
    
  choice=input("Do you want to enter another event?") 
if choice=="No":
  print("Thank you for using the event calendar.")
  #The program ends.


