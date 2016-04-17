import random

dice = {}

#initializes and resets the dice values
def init():
  global dice
  dice = {"WIN" : [7, 11], "LOSE" : 0}

#creates and combines two random values from 1 - 6
def roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1+dice2

#rolls the dice and returns true if the game continues, false if the game is won or lost
def play():
    test = roll()
    str = "You rolled "
    str += `test`
    if test in dice["WIN"]:
        showInformation(str +". You WIN!!")
        return False
    elif dice["LOSE"] == 0:
        print("setting Dice")
        dice["LOSE"] = dice["WIN"]
        dice["WIN"] = [test]
        showInformation(str +". You must not get 7 or 11")
        return True
    elif test in dice["LOSE"]:
        showInformation(str +". You Lose")
        return False
    else:
        showInformation(str +". Try again")
        return "Roll Again"

#Starts the game. This is the main function used to play the game.
def gameStart():
   go = True
   init()
   showInformation("Roll?")
   while go:
       go = play()
       if go == False:
         answer = requestString("Play again?")
         if answer == "yes" or answer == "Yes":
           go = True
           init()
         else:
           print("FIN")
         