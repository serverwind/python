from tkinter import*

root = Tk()
def myClick():
	myLabel = Label(root, text='hello')
	myLabel.pack()
myButton = Button(root, text='click me', command=myClick)
myButton.pack()

root.mainloop()
