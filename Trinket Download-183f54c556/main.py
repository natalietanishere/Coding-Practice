def CheckSystem(n,vowels):
  final=[each for each in n if each in vowels]
  print(len(final))
  print(final)



vowels='Aa,Ee,Ii,Oo,Uu'
n=input('Write a word in English')
CheckSystem(n,vowels)
