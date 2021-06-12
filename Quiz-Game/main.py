
from questions import quiz

def checkAnswers(x,answer,attempt,score):
  if quiz[x]['Answer'].lower() == answer.lower():#only accessing the question num and answer
     print("Correct answer! Your score is " + str(score + 1))
     return True
     
  else:
    attempt-=1
    print("Wrong answer. You have " + str(attempt) + " attempts left.")
    return False
    
score = 0
attempts = 3
for x in quiz: #x means index 0
   while attempts>0:
     print(quiz[x]['Question']) # ???? 
     answer = input("Enter answer here:")
     check = checkAnswers(x,answer,attempts,score)
     if check:
            score += 1
            break
            attempts -= 1 
    
 def fa_to_ce(x):
    x= (x-32) * 5/9
    y = round(x,2)
    return y
 print(fa_to_ce(66))
 #ctra a and then ctrl / gets all code becoming a part of a comment

# https://www.geeksforgeeks.org/binary-search/