from tkinter import*

root = Tk()
root.title = 'Password Manager'
root.geometry("300x300")

password = Entry(root)
password.grid(row = 0, column = 2)

def myFunc():
	if (password.get() == '123'):
		hello = Label(root, text='hello')
		hello.grid(row = 3, column = 2)

sendPass = Button (root, text='send',command=myFunc)
sendPass.grid(row = 2, column = 2)

root.mainloop()
