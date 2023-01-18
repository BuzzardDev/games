import random
import main

cpuChoices = ['Rock', 'Paper', 'Scissors']


def playAgain():
  again = input("Play Again? (Y/N) ")
  if again.lower() == "y":
    main.clear()
    game(False)
    wins = 0
    losses = 0
  else:
    main.clear()
    game(True)
    wins = 0
    losses = 0
    main.menu()


def game(gameOver=False):
  wins = 0
  losses = 0
  while (gameOver == False):
    print(f"Wins: {wins} \nLosses: {losses}")
    userInput = input("[Type: Rock, Paper, Scissors] ")
    computerInput = random.choice(cpuChoices)
    print(f"Your Play: {userInput.lower()}\nCPU Play: {computerInput.lower()}")
    # LOSSES
    if (userInput.lower() == "rock") and (computerInput.lower() == "paper"):
      losses += 1
    elif (userInput.lower() == "paper") and (computerInput.lower()
                                             == "scissors"):
      losses += 1
    elif (userInput.lower() == "scissors") and (computerInput.lower()
                                                == "rock"):
      losses += 1

    # WINS
    if (userInput.lower() == "paper") and (computerInput.lower() == "rock"):
      wins += 1
    elif (userInput.lower() == "scissors") and (computerInput.lower()
                                                == "paper"):
      wins += 1
    elif (userInput.lower() == "rock") and (computerInput.lower()
                                            == "scissors"):
      wins += 1
    elif (userInput.lower() == "q"):
      main.clear()
      main.menu()

    if wins == 2:
      print("You Win!")
      playAgain()

    elif losses == 2:
      print("You Lose!")
      playAgain()


if __name__ == '__main__':
  game(False)
