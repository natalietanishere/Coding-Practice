
word = "duck"#the word we have
guesses = ''#where to put guesses

lives = 4 #how many lives they have
while lives > 0: #the code runs until they lose        

    failed = 0 #you start off not failing because you did not start the game            

      
    for char in word:#the code compares the letters in the words with your guess     

        if char in guesses:    
    
            print char,#if you guess a correct letter, it is shown in that area
        else:
    
            print "_",  #try again   
       
            failed += 1  #you lose a life  

    if failed == 0:        
        print "You won"  #you win when you guess the word


        break #game ends             

    guess = raw_input("guess a character:") #the player is told this in the start

    guesses += guess #your number of guesses can change                   

    if guess not in word:  
 
        lives -= 1 #you lose 1 life per wrong guess       
 
        print "Wrong"
 
        print "You have", + lives, 'more guesses' #it shows how many guesses you have
 
        if lives == 0:           
    
            print "You Lose"
          