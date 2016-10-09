#!/usr/bin/env python3
#P3ETAE - The Python 3 Experimental Text Adventure Engine


import os
import sys
import json



# THIS IS AN EMPTY GLOBAL DICTIONARY THAT WILL BE USED TO STORE THE GAME WORLD DATA
rooms = {}



def main():
  clearTerminal()
  loadGameWorld()
  navigation()



def clearTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')



def loadGameWorld():
  engineName = 'P3ETAE: Python 3 Experimental Text Adventure Engine'
  usage = 'USAGE: ' + sys.argv[0] + ' [.json file]' 

  # CHECK IF JSON FILE HAS BEEN PROVIDED 
  if len(sys.argv) < 2:
    print (engineName)
    print ('No world data file.')
    print (usage) 
    quit()

  # CHECK IF JSON FILE EXISTS
  if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1], 'r') as fp:
      global rooms 
      rooms = json.load(fp)
  else:
    print (engineName)
    print ('Cannot find world data file.')
    print (usage) 
    quit()



def navigation():
  gameLoop = True

  # DEFINE THE COMMANDS THAT THE GAME ENGINE WILL RECOGISE
  legalCommands = ["north", "south", "east", "west"]

  # THIS IS THE PLAYER'S CURRENT ROOM IN THE GAME WORLD
  currentRoom = '1'

  while gameLoop == True:
    print ("You are in:", rooms[str(currentRoom)]["name"])
    # GET PLAYER INPUT
    move = input("Where do you want to go? ")
    move = str(move)
    # CHECK PLAYER ENTERED A LEGAL COMMAND
    if move not in legalCommands:
      print ("I only understand the following commands:", end=" ")
      for i in legalCommands:
        print (i, end=" ")
      print ("\n")
    # MOVE PLAYER TO NEW ROOM
    elif move in rooms[str(currentRoom)]:
      currentRoom = rooms[str(currentRoom)][move]
    else:
      print ("You can't go that way.")



if __name__ == "__main__":
  main()
