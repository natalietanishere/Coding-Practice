#Easy to read
ronum = {
  'I':1,
   'V':5,
    'X':10,
     'L':50,
      'C':100,
       'D':500,
        'M':1000
  }
def ronum_conversion(n):
  sum = 0
  for i in range(len(n)-1):
    l = n[i]
    r= n[i+1]
    if ronum[l] < ronum[r]:
      sum -= ronum[l]
    else:
      sum += ronum[l]
  sum += ronum[n[-1]]#if you remove the [], it reverts the order
  return sum
    

print(ronum_conversion('MXXI'))

#http://pythontutor.com/ 