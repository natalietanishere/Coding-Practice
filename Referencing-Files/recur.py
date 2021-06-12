

def recursive_method(num):
  def factorial(num):
    if num == 1:
      return 1
    else:
      return (num * factorial(num-1))
  if num<0:
    print("No factorials")
  


#def recur_factorial(num):
  #if num==1:
    #return num
 # else:
 ##   return num * recur_factorial(num-1)
#if num>0:
  #print("Sorry, factorials don't exist in negative numbers")
#elif num==0:
  #print("The factorial is 1")
#elif num<0:
  
