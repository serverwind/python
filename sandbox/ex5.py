#Задача 5.
#Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно. 

firstNum = int(input())
secondNum = int(input())

for firstNum in range(secondNum):
	print(firstNum+1)   
