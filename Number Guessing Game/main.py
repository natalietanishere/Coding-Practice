import random
#This uploads random numbers.

guessesTaken=0

myName=input("Hello! What's your name?")

number=random.randint(1,20)
print(myName +",I am thinking of a number between 1 and 20.")

while guessesTaken<6:
  print("Take a guess.")
  guess=input()
  guess=int(guess)
#You get 6 chances to guess the number.
  
  guessesTaken=guessesTaken+1
  
  if guess<number:
    print("Your guess is too low.")
  
  if guess>number:
    print("Your guess is too high.")
  
  if guess==number:
    break
#The while loop ends once you guess the number.
if guess==number:
   guessesTaken=str(guessesTaken)
   print("Wow! Good job, "+myName+"!You guessed my number in "+guessesTaken+" guesses!")
   
if guess!=number:
   number=str(number)
   print("Nah. The number I was thinking of was "+number+".")
#It tells you the correct answer.