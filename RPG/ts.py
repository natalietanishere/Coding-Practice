from ts_options import title_screen_options
import time 
import os 
def title_Screen():
  os.system("clear")
  #clears all text 
  print('#' * 45)
  print('# Welcome to this text-based puzzle RPG for #')
  print("#      natalie project     #")
  print('#' * 45)
  #45 hashtag signs that make a box
  print("                 .: Play :.                  ")
  print("                 .: Help :.                  ")
  print("                 .: Quit :.                  ")
  title_screen_options()

