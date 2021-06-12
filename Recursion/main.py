def recursion(n):
  return 1 if n == 1 else n * recursion(n-1)
recursion(4) #factorial 4
print(recursion(4))
  
  