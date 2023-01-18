import rpc
import ttt
import subprocess
gameChoices = [["Rock Paper Scissors", "rpc"], ["Tic-tac-toe", "ttt"]]

def clear():
  subprocess.call('clear', shell=True)

def menu():
  print("What games would you like to play?")
  for i in gameChoices:
    print(i[0] + " | command: " + i[1])

  gameSelection = input(": ")

  if gameSelection.lower() == "rpc":
    clear()
    rpc.game()
  elif gameSelection.lower() == 'ttt':
    clear()
    # ttt.setInput()
    ttt.game()
