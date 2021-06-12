a = [1,54,18,78,20]
for i in range(len(a)):
  d = i #helps go through list
  for j in range(i+1,len(a)): #finds the minimum element in a, sorts through the array
    if a[d]>a[j]: #checks the order
      d = j
  a[i],a[d] = a[d],a[i] #switches elements
for i in range(len(a)):
  print a[i]
#above is selection sort

print(" ")
print(" ")

for i in range(1,len(a)): #this is insertion sort
  ki = a[i] # the index
  j = i-1 # the real index, which is zero
  while j>=0 and ki<a[j]: #checks if the zero index is here, including ki
    a[j+1] = a[j] # so the index is 1
    j -= 1
  a[j+1] = ki
for i in range(len(a)):
  print a[i]

    

    

  
