from game_loop import main_game_loop
from game_loop import prompt

def examine():
    if room_solved[player1.position] == False:
        print('\n' + (cube[player1.position][INFO]))
        print((cube[player1.position][PUZZLE]))
        puzzle_answer = input("> ")
        checkpuzzle(puzzle_answer)
    else:
        print("There is nothing new for you to see here geesh")


def checkpuzzle(puzzle_answer):
        if player1.solves >= 5:
            endspeech = ("Without you having done anything, the key begins to rotate.\nIt begins to rain.\nAll of the sides of the box begin to crumble inwards.\nLight begins to shine through the cracks in the walls.\nA blinding flash of light hits you.\nYou have escaped!")
            for character in endspeech:
                sys.stdout.write(character) #stdout means standard output, sys is used to help systems understand the commands
                sys.stdout.flush()
                time.sleep(0.05)
            print("\nCONGRATULATIONS!")
            sys.exit()
        else:
            print("Nothing has happened. Oof")

          
    elif player1.position == 'south':
        if puzzle_answer == (player1.astrological):
            room_solved[player1.position] = True
            player1.solvemove_destinations += 1
            print("I Guess I Am The Candle, Huh? You're Just Using Me To Get Out Of This Cube, Huh? Don't Think I Don't See Through Your Smug Smile. Well, It Is Not Like I Can Do Anything. Go Through This Portal Or Whatever And Take My Eye With You.'He gives you his eye.")
            print("\nPuzzles solved: " + str(player1.solves))
        else:
            print("'Nope!' It bites you with venom.'Try Again!'\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
            examine()


    elif player1.position == 'top':
        if puzzle_answer == (player1.astrological):
            room_solved[player1.position] = True
            player1.solvemove_destinations += 1
            print("Ah yes, my friend Cake. I have this very convenient floss eraser that they made. You will visit them for me, right?' She uses a cherry to pick you out and gives it to you.")
            print("\nPuzzles solved: " + str(player1.solves))
        else: print("She sprays you with more radioactive candy floss. 'Try again!'")
        examine()


    elif player1.position == 'north':
        if puzzle_answer == (player1.astrological):
            room_solved[player1.position] = True
            player1.solvemove_destinations += 1
            print("'Well, uh, thanks for making this easier for me.'He hands you a key.")
            print("\nPuzzles solved: " + str(player1.solves))
        else:
          print("'I'm really sorry.'He bites your head off. Then, it traumatizingly grows back. 'Try again, I guess.'")
          examine()


    elif player1.position == 'ground':
        if puzzle_answer == (player1.astrological):
            room_solved[player1.position] = True
            player1.solvemove_destinations += 1
            print("'UH, YOU RE REALLY LUCKY THAT YOU ANSWERED CORRECTLY. I HATE WHISPERING. PROBABLY WOULD HAVE THROWN YOU INTO THE GARBAGE IF YOU GOT IT WRONG.' You hand her a key. 'WHAT AM I SUPPOSED TO DO WITH THIS??' The other ogre whispers to her. 'WOW, WE CAN FINALLY LEAVE THIS DUMP?.... WOW, I GUESS I ACTUALLY HAVE TO BE NICE TO YOU, DON T I ?... YOU KNOW WHAT? NAH. YOU CAN GO THO WITH THIS SOGGY FLOWER.'She gives you a soggy flower. ")
            print("\nPuzzles solved: " + str(player1.solves))
        else:
          print("'OKAY. GO JOB!' She punches you in the face and splashes trash on you. 'TRY AGAIN AND STOP WASTING MY TIME!'")


   # else:
        #if puzzle_answer == (cube[player1.position][SOLVED]):
          #  room_solved[player1.position] = True
           # player1.solvemove_destinations += 1
           # print("You have solved the puzzle. Onwards!")
           # print("\nPuzzles solved: " + str(player1.solves))
       # else:
            #print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #examine()