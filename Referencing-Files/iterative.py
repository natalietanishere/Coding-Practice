def iterative_fact(num):
  fact=1
  if num<0:
   print("no factorial")
  if num == 0:
   print("factorial is 0")
  else:
   for i in range(1,num + 1):
     fact = fact*i
   print("factorial", num, "is",fact)