import random
n=random.randint(1,10)
guess=int(input('Guess the number'))

while n!= guess:
  if guess>n:
    guess=int(input('Your guess is too big.'))
  elif guess<n:
    guess=int(input('Your guess is too small.'))
  elif guess==n:
    guess=('Yay! Your guess is correct!')
  else:
   print('That is not a number!')
   break







print(n)

