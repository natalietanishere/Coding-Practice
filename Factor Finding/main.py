number= int(input('Give me a number and I will find the factors.'))
def factor_finding(x):
  print('the factors are ',x)
  for i in range(1,x+1):
    if x%i==0:
      print(i)
    
    
  
factor_finding(number)
