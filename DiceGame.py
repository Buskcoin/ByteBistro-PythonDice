import random
#holds the dice informaion
dice = {}
canvas = makeEmptyPicture(250,150)

#initializes and resets the dice values
def init():
  global dice
  dice = {"WIN" : [7, 11], "LOSE" : 0}
  addRectFilled(canvas, 0,0, getWidth(canvas), getHeight(canvas), white)
  repaint(canvas)
  show(canvas)

#creates and combines two random values from 1 - 6
def roll():
    dice1 = random.randint(1,6)
    showDie(dice1, 0)
    dice2 = random.randint(1,6)
    showDie(dice2, 120)
    return dice1+dice2
    
    
def showDie(i,  pos):
  file = "C:\Users\Bob\Documents\CSUMB\Python\Labs\Lab15\dice"
  file += `i`
  file += ".PNG"
  die = makePicture(file)
  copyInto(makePicture(file), canvas, 1+pos,1)
  repaint(canvas)

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
        showWarning(str +". You must not get 7 or 11")
        return True
    elif test in dice["LOSE"]:
        showError(str +". You Lose")
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
         global canvas                  
         myFont = makeStyle(sansSerif, bold, 25)
         addTextWithStyle(canvas, 50,50,"GAME OVER", myFont, orange)
         repaint(canvas)
         answer = requestString("Play again?")
         if answer == "yes" or answer == "Yes":
           go = True
           init()
         else:
           print("FIN")
           
         