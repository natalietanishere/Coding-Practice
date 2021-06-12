print("Welcome to Sally's Sandwich Shop!")
cost = 0
print("Sizes: Big : $15 Medium : $10  Small: $5")
size = input("What size would you want?")
if size == "Big":
    cost = 15
elif size == "Medium":
    cost = 10
elif size =="Small":
   cost = 5
else:
   print("I'm giving you a medium.")
   cost = 10
cheese = input("Do you want cheese?")
toppings = 0
if cheese == "Yes" or cheese =="yes":
   toppings += 1
   toppings_string = "cheese"
ham = input("Do you want ham?")
if ham == "Yes" or ham =="yes":
   toppings += 1
   toppings_string += "ham"
cost += toppings * 1.25
print(cost)
print(toppings_string)
 
   
   