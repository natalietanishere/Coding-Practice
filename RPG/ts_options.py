from setu import setup_game
from setu import help_menu
def title_screen_options():
  option = input("$")
  if option.lower() == "play":
    setup_game()
  elif option.lower() == "quit":
    sys.exit()#designed to stop programs 
  # exit code 0 is successful, code 1 means error
  elif option.lower() == "help":
    help_menu() #defined later
  while option.lower() not in ['play','help','quit']:
    print("invalid command, try again")
    option = input("$")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "quit":
        sys.exit()
    elif option.lower() == "help":
        help_menu()
  