the_dict = {"popcorn":"kernel", "cotton candy":"sugar", "candy cane":"peppermint"}
#keys, values, and items
#items give the key and value
my_item = the_dict.items()
print(my_item)
for key in the_dict.keys():
  print(key)
for value in the_dict.values():
  print(value)
sugar = 'sugar' in the_dict.values() # this condition is called membership test
print(sugar)
glucose = 'sugar' in the_dict.keys()
print(glucose)
#membership tests are good for testing errors or if you have many items



  