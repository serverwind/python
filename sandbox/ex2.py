#Задание 2: Даны три целых числа. Определите, сколько среди них совпадающих. 
#Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны). 

x = input('first num: ')
y = input('second num: ')
z = input('third num: ')

firstNum = int(x)
secondNum = int(y)
thirdNum = int(z)

if (x == y and x == z):
	print('all numbers are the same')
elif (x == y or x == z or y == z):
	print('only 2 numbers are the same')
else:
	print('all numbers are different')
