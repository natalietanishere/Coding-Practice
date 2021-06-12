from ts import title_Screen
from ts_options import title_screen_options
from setu import setup_game
from setu import help_menu
import time 
import os 
  # operation system commands 
import sys 
  # means system, used with os
screenWidth = 100
'''
----------------------------------------------------
        North -v      _.-+							
                 _.-""     '						
             +:""            '						
             | \  v Top Side   '					
              | \             _.-+					
              |  '.       _.-"   |					
    West -->  |    \  _.-"       |  <-- East  	
               |    +"           |	 		
               +    | South->    | 					
                \   |          .+ 				
                 \  |       .-'					
                  \ |    .-'	<-- Ground/Center		
                   \| .-'							
                    +'   							
-----------------------------------------------------
'''

class player() :
  def __init__(self): 
    #__init__ is a constructor (creating a mold to fit in variables), beneficial for repetitive tasks 
      self.name = "" 
      self.position = "ground"
      self.won = False
      self.solves = 0
  player_one = player()
  #local var more secure since they are only in a certain function
  Description = "description"
  Info = "info"
  Puzzle = "puzzle"
  Solved = False
  side_Up = "up","forward"
  side_Down = "down","back"
  side_Left = "left",
  side_Right = "right",
    #Python uses snake_case, most languages use camelCase,old languages use Pasca
  room_Solved = {
    "top": False ,
    "north": False ,
    "ground": False ,
    "south": False,
    "west": False,
    "east": False 
    }
    #if a key isn't global, should be in quotes
  cube = {
    "top" : {
      Description : "You find yourself floating on a cloud. Everything is a pastel color, but there is never-ending nuclear explosion of some sorts going on. Luckily, you are far away from this, but you float to the edge of the cube and, oh no! The clouds were made of cotton candy and are now melting! You are now stuck in radioactive candy floss.",
      Info : "You meet a bon bon." ,
      Puzzle: "'Greetings. I see you are in a devastating predicament. Ah, your greivances are understandable. Tell me, what am I describing? Sweet, gentle, and airy. Sometimes we all need him. After all, no triumph It does not pass without him. Who is he?'" ,
      Solved:"cake" ,
      #Reaction "Ah yes, my friend Cake. I have this very convenient floss eraser that they made. You will visit them for me, right?' She uses a cherry to pick you out and gives it to you."
      side_Up: "north",
      side_Down : "south",                                   
      side_Left:  "east",
      side_Right: "west"
      },
      "north" : {
        Description : "You find yourself in an icy tundra, filled with snow and wannabe yetis.",
        Info : "Out of the snow, a fluffy soot monster wearing plastic iscicles and a hat that says 'You alrYETI know.' ",
        Puzzle:"'Hi,uh do you like my punny hat? .....no? Well uh, apparently, I am supposed to uh give you a riddle or something. Um..' He picks up a crumbly notecard. 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'" ,
        Solved:"an echo"  ,
      # Reaction:"'Well, uh, thanks for making this easier for me.'He hands you a key.",
      side_Up:"top",
      side_Down :"ground",
      side_Left:"west",
      side_Right: "east"
      },
      "ground": {
        Description : "You find yourself in a dark forest with only trees and one tiny cottage drifting in the distance. You dash to the house, but apparently, it is occupied.",  
        Info : "An ogre approaches you. 'HEY. GET OUT OF OUR YARD.' You stay. 'GET OUT OR WE LL THROW YOU TO THE WOLVES.' You stay. 'WHAT? WE RE NOT GOING TO EAT YOUR DISGUSTING HEAD. WE HAVE STANDARDS.' You stay with a sad pout on your face. 'YOU REALLY SHOULD VE GOT OUT WHEN YOU HAD THE CHANCE. ANSWER THIS RIDDLE OR ELSE.'",
        Puzzle: "'I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?'",
        Solved:"a map" ,
      # Reaction:"'UH, YOU RE REALLY LUCKY THAT YOU ANSWERED CORRECTLY. I HATE WHISPERING. PROBABLY WOULD HAVE THROWN YOU INTO THE GARBAGE IF YOU GOT IT WRONG.' You hand her a key. 'WHAT AM I SUPPOSED TO DO WITH THIS??' The other ogre whispers to her. 'WOW, WE CAN FINALLY LEAVE THIS DUMP?.... WOW, I GUESS I ACTUALLY HAVE TO BE NICE TO YOU, DON T I ?... YOU KNOW WHAT? NAH. YOU CAN GO THO WITH THIS SOGGY FLOWER.'She gives you a soggy flower. ",
      side_Up:"north",
      side_Down : "south",
      side_Left:"west",
      side_Right: "east"
      },
      "south": {
        Description : "You find yourself stranded in the desert. A snake slithers past you. " ,
        Info : "'Hello, Human. How Are You?'You stare at them with your beady eyes, waiting for a riddle. 'How rude! You are not going to ask ME --- wait, I Have To Talk Like This.",
        Puzzle:"'Well, Here's Your Riddle, You Jerk: You measure my life in hours and I save you by expiring. I'm quick when I am thin and slow when I'm fat. The wind is my enemy. What am I?'" ,
        Solved:"a candle"  ,
      #Reaction "I Guess I Am The Candle, Huh? You're Just Using Me To Get Out Of This Cube, Huh? Don't Think I Don't See Through Your Smug Smile. Well, It Is Not Like I Can Do Anything. Go Through This Portal Or Whatever And Take My Eye With You.'He gives you his eye."
      side_Up:"ground",
      side_Down : "top",
      side_Left: "west",
      side_Right:"east"
      },
      "west": {
        Description : " You find yourself in the sterotypical Wild West with screeching cowboys barking left and right.",
        Info : "'HiYA tHEre, FeLLa. NaME s WhOe. I M oNe Of da MOst FAmus oF da bois. I HaaVE da SPECIpal Haonor ta GIve ya A RRRRIddle. MaaN, I Wuv rrrrOlling my RRRRS.'",
        Puzzle:"'Wut DissApEaRS aS SooN As ya SAY iTSS Name?'You look at them, confused. 'Wut? DiD ya ExPEcct ME to TAlk lik ya wHEn sAAyiNg da RIddLE?'" ,
        Solved:"silence",
      # Reaction:"'WaLL bee, Ya SoLvED it. GOod fAA ya. Taake mi SHooe as A reWAArd.'They give you a stinky shoe.",
      side_Up:"north",
      side_Down :"south",
      side_Left:"top",
      side_Right:"ground"
      },
      "east": {
        Description : "You find yourself in a city made out of waterfalls. Pearls glisen your steps, and you smell a salty ocean breeze come your way. A mermaid comes up to you." ,
        Info :"Hello, fellow. I am Pearla. Creative name, huh? I came up with this name myself!!! Ahem, anyway, solve this and I will give you this cute seashell I created. Did you know that I invented seashells?'" ,
        Puzzle:"'What gets wet while drying?''" ,
        Solved:"a towel",
        #Reaction:"'Congrats! You are almost as smart as me! Anyways, here is your absolutely beautiful shell. I think we will be best friends!'She gives you a shell covered with plastic chip bags, turtle vomit, and oil.",
      side_Up:"north",
      side_Down : "south",
      side_Left: "ground",
      side_Right: "top"
      }
    }
  title_Screen()

