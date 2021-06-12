the_dict = {"popcorn":"kernel", "cotton candy":"sugar", "candy cane":"peppermint"}
empty = {}
for key,value in the_dict.items():
  empty[value] = key #switches keys and values
print(empty)
balloon = {"red": 3, "blue" : 5, "purple": 8}
blank = {}
for i in (the_dict, balloon):
  blank.update(i) #combines dicts
print(blank)
#sorted sorts by ascending order
#type sorted(dict)

  
