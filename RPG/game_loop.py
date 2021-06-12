from exam import examine
from moo import move
import time 
import os 
import sys

def main_game_loop():
  puzzles = 6
  while player_one.won == False:
    prompt()

def prompt():
  print("what would you like to do?")
  if player_one.solves == 5:
    print("The world starts to shake. Hmmm..maybe it's going to a party?") 
  action = input("$")
  acceptable_actions = ['move','go','travel','walk','inspect','examine','look','search']
  while action.lower() not in acceptable_actions:
      print("Wut, can you say that again?")
      action = input("$")
  if action.lower() == "quit":
     print("Ok")
     sys.exit()
  elif action.lower() == ['move','go','travel','walk']:
        move()
  elif action.lower() == ['inspect','examine','look','search']:
        examine()    