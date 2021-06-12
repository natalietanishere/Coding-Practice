#data structures:

#primitive: only one piece, all user-defined
#primitive examples :int, float(with decimals), 
#str, boolean (conditional statments, True or False)

#non-primitive: categorzing similar primitive data, built into Python
#non-primitive examples: a list, dictionary, set, tuple,
#stack, queue, tree, graph, max and min heap

list = ["here","there","where","tear","hair"]
print(list)
#lists can have many types of primitive data next to each other, mutable
#can be named list, but you shouldn't

print(list[1])#prints there, index has to be int

print(list[-1])#goes right to left, 0 is empty in this case
#important for adding data

print(list[1:3])#called slice, choose which indexes you want to start and end with
#does not include last index

list[3] = "care" #change index by defining it like a variable
print(list)

list.pop(3)#removes this index
print(list)

list.append("mare")#adds an index, great for putting user input into list
print(list)

list[0:3] = "where are we","we are here" #reassigns different value to certain indexes
print(list)


alphabet = ("a","b","c")
#this is a tuple
#tuple is irrechangeable
print(alphabet)
#good when you don't want the value to change, great for security 

bee = 1 , 2 , 3 #this is automatically a tuple
print(bee)

print(type(alphabet))
print(type(bee))

numbers = [1,2,"one","two"]
print(type(numbers[1]))
print(str(numbers))



readysetgo = {1,1,2,3}
print(readysetgo)
#this is a set
#sets are mutable, cannot be duplicable, NO index

readysetgo.add(4)#when appending sets, use add
#add just adds the value at the end of set
print(readysetgo)


grades = {"Sally":90, "Bob":80,"Kathy":89}
#this is a dict
#dicts have keys and values, NO index
#can store and change values, NO duplicates
print(grades)

grades["Sally"] = 80
print(grades)



