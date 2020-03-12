#Задание 1: Даны два целых числа. Выведите значение наименьшего из них. 

x = input('first num: ')
y = input('second num: ')
firstNum = int(x)
secondNum = int(y)

if (x < y):
	print(x + ' < ' + y)
elif (x > y):
	print(x + ' > ' + y)
else:
	print(x + ' = ' + y)
