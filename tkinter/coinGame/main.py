#ALPHA

import random
from tkinter import*

root = Tk()
root.title = 'Drop Coin'
root.geometry("300x300")

hello = Label (root, text = 'Hello! Lets play the game with me.')
hello.pack()

def myFunc():
	playerDrop = random.randint(1, 2)
	aiDrop = random.randint(1, 2)
	if (playerDrop > aiDrop):
		playerWin = Label(root, text='You win!')
		playerWin.pack()
	elif (playerDrop < aiDrop):
		playerLost = Label(root, text='You lost!')
		playerLost.pack()
	else:
		itsDraw = Label(root, text='Its draw!')
		itsDraw.pack()
	
letsPlay = Button(root, text = 'play', command = myFunc)
letsPlay.pack()

root.mainloop()
