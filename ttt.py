import random
import main
import time

# options for cpu to use X or O
cpuOptions = ["X","O"]

#cpuGrid Location



# array of choices for cpu to choose
array = ["top left", "top middle", "top right",
               "middle left", "middle", "middle right",
               "bottom left", "bottom middle", "bottom right"]
# player selections
array2D = [["top left", "top middle", "top right"],
               ["middle left", "middle", "middle right"],
               ["bottom left", "bottom middle", "bottom right"]]
cpuLocation = array

userOptions = array2D

gameBoard = [["☐","☐","☐"],
             ["☐","☐","☐"],
             ["☐","☐","☐"]]

userOption = None
cpuGridLocation = None
userLocation = None

top = ["top left", "top middle", "top right"]
middle = ["middle left", "middle", "middle right"]
bottom = ["bottom left", "bottom middle", "bottom right"]

def listOptions():
  for i in userOptions:
      print(f"\n{i}")
  

def game(gameOver = False):
  global userOption
  global cpuGridLocation
  global userLocation
  cpuChoice = None
  while gameOver == False:
    for i in gameBoard:
      # print(i)
      print(' '.join(i))
    if userOption is None:
      userOption = input("Type X or O: ")
      cpuOptions.remove(userOption.upper())

      # top row
    if (gameBoard[0][0] == userOption.upper()) and (gameBoard[0][1] == userOption.upper()) and (gameBoard[0][2] == userOption.upper()):
        main.clear()
        print("You Win")
      #middle row
    elif (gameBoard[1][0] == userOption.upper()) and (gameBoard[1][1] == userOption.upper()) and (gameBoard[1][2] == userOption.upper()):
        main.clear()
        print("You Win")
      #bottom row
    elif (gameBoard[2][0] == userOption.upper()) and (gameBoard[2][1] == userOption.upper()) and (gameBoard[2][2] == userOption.upper()):
        main.clear()
        print("You Win")
      # down left
    elif (gameBoard[0][0] == userOption.upper()) and (gameBoard[1][0] == userOption.upper()) and (gameBoard[2][0] == userOption.upper()):
        main.clear()
        print("You Win")
      # down middle
    elif (gameBoard[0][1] == userOption.upper()) and (gameBoard[1][1] == userOption.upper()) and (gameBoard[2][1] == userOption.upper()):
        main.clear()
        print("You Win")
      # down right
    elif (gameBoard[0][2] == userOption.upper()) and (gameBoard[1][2] == userOption.upper()) and (gameBoard[2][2] == userOption.upper()):
        main.clear()
        print("You Win")
      #diagnal
    elif (gameBoard[0][0] == userOption.upper()) and (gameBoard[1][1] == userOption.upper()) and (gameBoard[2][2] == userOption.upper()):
        main.clear()
        print("You Win")

    # lose
    # top row
    if (gameBoard[0][0] == cpuChoice) and (gameBoard[0][1] == cpuChoice) and (gameBoard[0][2] == cpuChoice):
        main.clear()
        print("You Lose")
      #middle row
    elif (gameBoard[1][0] == cpuChoice) and (gameBoard[1][1] == cpuChoice) and (gameBoard[1][2] == cpuChoice):
        main.clear()
        print("You Lose")
      #bottom row
    elif (gameBoard[2][0] == cpuChoice) and (gameBoard[2][1] == cpuChoice) and (gameBoard[2][2] == cpuChoice):
        main.clear()
        print("You Lose")
      # down left
    elif (gameBoard[0][0] == cpuChoice) and (gameBoard[1][0] == cpuChoice) and (gameBoard[2][0] == cpuChoice):
        main.clear()
        print("You Lose")
      # down middle
    elif (gameBoard[0][1] == cpuChoice) and (gameBoard[1][1] == cpuChoice) and (gameBoard[2][1] == cpuChoice):
        main.clear()
        print("You Lose")
      # down right
    elif (gameBoard[0][2] == cpuChoice) and (gameBoard[1][2] == cpuChoice) and (gameBoard[2][2] == cpuChoice):
        main.clear()
        print("You Lose")
      #diagnal
    elif (gameBoard[0][0] == cpuChoice) and (gameBoard[1][1] == cpuChoice) and (gameBoard[2][2] == cpuChoice):
        main.clear()
        print("You Lose")
    listOptions()
    userLocation = input("Choose a location: ")

    # TOP
    if userLocation.lower() == "top left":
      gameBoard[0][0] = userOption.upper()
      userOptions[0].remove("top left")
      cpuLocation.remove("top left")
      main.clear()
    elif userLocation.lower() == "top middle":
      gameBoard[0][1] = userOption.upper()
      userOptions[0].remove("top middle")
      cpuLocation.remove("top middle")
      main.clear()
    elif userLocation.lower() == "top right":
      gameBoard[0][2] = userOption.upper()
      userOptions[0].remove("top right")
      cpuLocation.remove("top right")
      main.clear()

    # MIDDLE
    if userLocation.lower() == "middle left":
      gameBoard[1][0] = userOption.upper()
      userOptions[1].remove("middle left")
      cpuLocation.remove("middle left")
      main.clear()
    elif userLocation.lower() == "middle":
      gameBoard[1][1] = userOption.upper()
      userOptions[1].remove("middle")
      cpuLocation.remove("middle")
      main.clear()
    elif userLocation.lower() == "middle right":
      gameBoard[1][2] = userOption.upper()
      userOptions[1].remove("middle right")
      cpuLocation.remove("middle right")
      main.clear()

    # BOTTOM
    if userLocation.lower() == "bottom left":
      gameBoard[2][0] = userOption.upper()
      userOptions[2].remove("bottom left")
      cpuLocation.remove("bottom left")
      main.clear()
    elif userLocation.lower() == "bottom middle":
      gameBoard[2][1] = userOption.upper()
      userOptions[2].remove("bottom middle")
      cpuLocation.remove("bottom middle")
      main.clear()
    elif userLocation.lower() == "bottom right":
      gameBoard[2][2] = userOption.upper()
      userOptions[2].remove("bottom right")
      cpuLocation.remove("bottom right")
      main.clear()

    cpuChoice = random.choice(cpuOptions) # selects X or O
    # cpuGridLocation = botAI() # selects random location on grid
    # random.choice(cpuLocation)
    botAI()

    # TOP
    if cpuGridLocation.lower() == "top left":
      time.sleep(1)
      gameBoard[0][0] = cpuChoice.upper()
      userOptions[0].remove("top left")
      cpuLocation.remove("top left")
      main.clear()
    elif cpuGridLocation.lower() == "top middle":
      time.sleep(1)
      gameBoard[0][1] = cpuChoice.upper()
      userOptions[0].remove("top middle")
      cpuLocation.remove("top middle")
      main.clear()
    elif cpuGridLocation.lower() == "top right":
      time.sleep(1)
      gameBoard[0][2] = cpuChoice.upper()
      userOptions[0].remove("top right")
      cpuLocation.remove("top right")
      main.clear()

    # MIDDLE
    elif cpuGridLocation.lower() == "middle left":
      time.sleep(1)
      gameBoard[1][0] = cpuChoice.upper()
      userOptions[1].remove("middle left")
      cpuLocation.remove("middle left")
      main.clear()
    elif cpuGridLocation.lower() == "middle":
      time.sleep(1)
      gameBoard[1][1] = cpuChoice.upper()
      userOptions[1].remove("middle")
      cpuLocation.remove("middle")
      main.clear()
    elif cpuGridLocation.lower() == "middle right":
      time.sleep(1)
      gameBoard[1][2] = cpuChoice.upper()
      userOptions[1].remove("middle right")
      cpuLocation.remove("middle right")
      main.clear()

    # BOTTOM
    elif cpuGridLocation.lower() == "bottom left":
      time.sleep(1)
      gameBoard[2][0] = cpuChoice.upper()
      userOptions[2].remove("bottom left")
      cpuLocation.remove("bottom left")
      main.clear()
    elif cpuGridLocation.lower() == "bottom middle":
      time.sleep(1)
      gameBoard[2][1] = cpuChoice.upper()
      userOptions[2].remove("bottom middle")
      cpuLocation.remove("bottom middle")
      main.clear()
    elif cpuGridLocation.lower() == "bottom right":
      time.sleep(1)
      gameBoard[2][2] = cpuChoice.upper()
      userOptions[2].remove("bottom right")
      cpuLocation.remove("bottom right")
      main.clear()
      
    


      




def botAI():
  global cpuOptions
  global userLocation
  global userOption
  global cpuGridLocation
  global cpuLocation
  aiChoice = []
  aiChoice.append("random")
  aiChoice.append(cpuGridLocation)
  # this is supposted to allow the bot to place in middle left with a 50 50 chance
  if userLocation.lower() == "top left":
    if "middle left" in cpuLocation:
      if random.choice(aiChoice) == "random":
       print("works")
       cpuGridLocation = random.choice(cpuLocation)
       return cpuGridLocation
      else:
        cpuGridLocation = cpuLocation[3]
        return cpuGridLocation
        




if __name__ == '__main__':
  game(False)