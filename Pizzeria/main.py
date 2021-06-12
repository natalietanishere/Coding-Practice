name_input= input("Welcome to the Pizzeria! What is your name?")
print ("Our pizza size is 12 inches. Our classic cheese pizza costs only 5.99 plus tax!")
print("Toppings:")
print("Pepperoni Olives Pineapples Peppers Extra Cheese (Each topping is an extra $0.25.)")
cost=5.99
toppings_list=["Pepperoni","Olives","Pineapples","Peppers","Extra Cheese" ]
toppings_input=input("What toppings would you like? You can get up to five toppings.")
for toppings_list in toppings_input:
  cost+=.25
  if toppings_input==("None","none"):
    continue
tax=round(cost*.0775,2)
final_cost=cost+tax
print final_cost
print name_input
print("Thank you for buying our pizza.")


