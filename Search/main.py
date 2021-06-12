import time 
start_time = time.time()
def linear(array,n,x):
  for i in range(0,n):
    if array[i] == x:
      return i
  return -1 #no results
arg = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147]
print(arg)
x = int(input("Select a number from the array."))
n = len(arg)
print(linear(arg,n,x)) #prints index

def binary(array,l,r,x): #l and r are left and right of array
    while l <= r:
      mid = l + (r-l)// 2 #gives an integer
      if array[mid] == x:
        return mid
      elif array[mid] < x:
        l = mid + 1 #ignores left half AND middle
      else:
        r = mid - 1 #ignores right side AND middle
    return -1  
print(binary(arg,0,len(arg)-1,x))
print(time.time()- start_time)