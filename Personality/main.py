import random
personalities = ['kind','smart','clumsy','ignorant','mean','selfish','caring']
while True:
  start = input("Press e to exit.")
  if  start == "E" or start == "e" :
    exit(0) # built in error status , can't write a variable called exit
  # exit(0) means the code runs correctly, exit(1) means there is error
  else:
    print("You are " + random.choice(personalities))
  