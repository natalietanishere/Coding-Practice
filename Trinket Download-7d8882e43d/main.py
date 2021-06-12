for i in range(1,100):
  prime_flag= True
  for divisor in range(2,i-1):
    if i%divisor==0:
      prime_flag= False
      break
  if prime_flag:
    print i
