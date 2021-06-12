from ts import title_Screen
from game_loop import main_game_loop
import time
import os
import sys 

def setup_game():
  os.system('clear')#sends message to terminal to clear the line
  question1 = "Hey! What's your name?"

  for ch in question1:
    sys.stdout.write(ch)
    sys.stdout.flush()
   #every character written will be on screen
    time.sleep(0.05) 
  #spells out your name slowly, looks cool in games like Undertale

  name = input("$")
  player_one.name = name

  question3 = ("Well," + player_one.name + ",")
  for ch in question3:
    sys.stdout.write(ch)
    sys.stdout.flush()
    time.sleep(0.05)
  main_game_loop()
  
def help_menu():
  print("You are trapped in this cube with a bunch of pathetic plebs.\n") # \n is like br in HTML 
  print("Type which direction you want to go (Up, Down, Right, Left)\n")
  print("Navigate throughout the cube and answer riddles to get out. \n")
  print("I highly doubt that you have the capabilities to answer these impossible puzzles, but good luck!\n")
  title_Screen()
  