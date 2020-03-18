#WAGE HELPER v1.1
#Author: Alex Lestrange
#lestrangeqq@gmail.com

from tkinter import *

#Настройка главного окна
root = Tk()
root.title('Wage Helper')
root.config(bg='black')
root.geometry('600x300')
root.resizable(False, False)  #запрет на возможность ресайза окна юзером

#В разработке. Идея с добавлением как бы окна загрузки программы, которое будет пропадать через 3 секунды и появится основное меню программы.
#label_text = Label(root, text="hello world")

#def on_after():
#    label_text.configure( text="hello")

#label_text.pack()
#label_text.after(3000, on_after)

#Приветствие
hello = Label(root, text = 'Wage Helper')
hello.pack()
hello.config(font=("Verdana", 35), bg='black', fg='white')

#Поле ввода суммы
wage = Entry(root)
wage.pack()

#Функция рассчёта денег
#.config делает чтобы текст обновлялся, а не спамился один за одним после каждого нажатия
#self здесь нужен для того чтобы функция выполнялась по нажатию Enter
def calcFunc(self):
	half = int(wage.get()) / 2
	halfWage.config(text = 'Ограничьте свои нужды до: ' + str(half), font=("Verdana", 12), bg='black', fg='white')
	halfWage.pack()
	
	thirty = int(wage.get()) / 100 * 30
	thirtyWage.config(text = 'Ограничьте траты на желаемое до: ' + str(thirty), font=("Verdana", 12), bg='black', fg='white')
	thirtyWage.pack()
	
	twenty = int(wage.get()) / 100 * 20
	twentyWage.config(text = 'Отложите: ' + str(twenty), font=("Verdana", 12), bg='black', fg='white')
	twentyWage.pack()
	
#Функция расчета денег по клику на кнопку "Рассчитать" (тк я не нашел способа чтобы одна функция работала и по клику на кнопку и по нажатию Enter)
def calcFunc2():
	half = int(wage.get()) / 2
	halfWage.config(text = 'Ограничьте свои нужды до: ' + str(half), font=("Verdana", 12), bg='black', fg='white')
	halfWage.pack()
	
	thirty = int(wage.get()) / 100 * 30
	thirtyWage.config(text = 'Ограничьте траты на желаемое до: ' + str(thirty), font=("Verdana", 12), bg='black', fg='white')
	thirtyWage.pack()
	
	twenty = int(wage.get()) / 100 * 20
	twentyWage.config(text = 'Отложите: ' + str(twenty), font=("Verdana", 12), bg='black', fg='white')
	twentyWage.pack()

halfWage = Label (root, text = 'Ограничьте свои нужды до: ')
halfWage.pack()	
halfWage.config(font=("Verdana", 12), bg='black', fg='white')
thirtyWage = Label (root, text = 'Ограничьте траты на желаемое до: ')
thirtyWage.pack()
thirtyWage.config(font=("Verdana", 12), bg='black', fg='white')
twentyWage = Label (root, text = 'Отложите: ')
twentyWage.pack()
twentyWage.config(font=("Verdana", 12), bg='black', fg='white')

calculate = Button(root, text = 'Рассчитать', command = calcFunc2)
wage.bind('<Return>', calcFunc)  #биндим выполнение функции по нажатию на Enter
calculate.pack()

root.mainloop()
