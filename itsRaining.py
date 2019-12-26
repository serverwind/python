#name: itsRaining 1.0
#author: Lestra 26.12.19
#description: Пример выполнения программы работающей с IF ELSE и WHILE
#e-mail: lestrangeqq@gmail.com

print ('Please answer Yes or No')
rain = input ('It\'s raining? ')

if (rain == 'yes' or rain == 'YES' or rain == 'Yes'):
	umbrella = input ('Do you have umbrella? ')
	if (umbrella == 'yes' or umbrella == 'YES' or umbrella == 'Yes'):
		print ('Take umbrella')
	else:
		while (rain == 'yes'):  #запускаем цикл, который будет переспрашивать идет ли еще дождь, пока юзер не ответит 'no'
			print ('Wait for a while')
			rain = input ('It\'s still raining? ')
			if (rain == 'no' or rain == 'NO' or rain == 'No'):
				print('Go outside')
else:
	print ('Go outside')
