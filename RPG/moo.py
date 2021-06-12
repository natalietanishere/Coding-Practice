from game_loop import main_game_loop
from game_loop import prompt
def move(action):
    string = "What direction would you" + action + "to?"
    destination = input(string).lower()
    if destination == "forward":
      move_desination = cube[player_one.position][side_Up]
      move_player(move_destination)
    if destination == "backward":
      move_desination = cube[player_one.position][side_Down]
      move_player(move_desination)
    if destination == "right":
      move_desination = cube[player_one.position][side_Right]
      move_player(move_desination)
    if destination == "left":
      move_desination = cube[player_one.position][side_Left]
      move_player(move_desination)
    else:
      print("I don't know where you want to go.")
      move(theAction)
def move_player(move_destination):
    print("You moved to" + move_destination)
    player_one.position = move_destination
    print_location()
def print_location():
  print('\n' + ('#' * (4 +len(player_one.position))))
  print('# ' + player_one.position.upper() + ' #')
  print('#' * (4 +len(player_one.position)))
  print('\n' + (cube[player_one.position][DESCRIPTION]))