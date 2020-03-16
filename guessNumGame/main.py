#Игра - Угадай число (v1.2.2)
#Alex Lestrange 2020
#lestrangeqq@gmail.com

import random

num = random.randint(1, 20)
print('Привет! Давай играть.')
print('Угадай число от 1 до 20!')
difficulty = input('Выбери уровень сложности:\n [E]asy: 9 попыток \n [M]edium: 7 попыток \n [H]ard: 4 попытки\n')
if (difficulty == 'E') or (difficulty == 'e'):
	tryNum = 9
elif (difficulty == 'M') or (difficulty == 'm'):
	tryNum = 7
elif (difficulty == 'H') or (difficulty == 'h'):
	tryNum = 4

answer = None	#объявляем переменную без содержимого.

while answer != num and tryNum > 0:
	if (difficulty == 'E') or (difficulty == 'e'):
		print('\nУровень сложности: Easy. Попыток: ' + str(tryNum))
	elif (difficulty == 'M') or (difficulty == 'm'):
		print('\nУровень сложности: Medium. Попыток: ' + str(tryNum))
	elif (difficulty == 'H') or (difficulty == 'h'):
		print('\nУровень сложности: Hard. Попыток: ' + str(tryNum))
	
	answer = input('\nЯ думаю это ')
	answer = int(answer)

	if (answer == num):
		print('\nОтвет правильный, ты победил!;)')
	elif (answer < num):
		print('\nЭто число больше загаданного!')
		tryNum -= 1
		if (tryNum > 0):
			print('Осталось ' + str(tryNum) + ' попыток!')
		else:
			print('\nТы проиграл:( Загаданным числом было ' + str(num))
	elif (answer > num):
		print('\nЭто число меньше загаданного!')
		tryNum -= 1
		if (tryNum > 0):
			print('Осталось ' + str(tryNum) + ' попыток!')
		else:
			print('\nТы проиграл:( Загаданным числом было ' + str(num))
	else:
		print('Ошибка. Число должно быть от 1 до 20.')
