#Подкидыватель монеток
#Создайте программу, которая будет выводит случайно 0 или 1.
#Вместо 0 и 1, выводите “орёл” или “решка”.
#Добавьте цикл, чтобы программа так делала 50 раз.
#Выведите на экран, сколько раз выпал орёл и сколько - решка. 

import random

orel = 0
reshka = 1
orelScore = 0
reshkaScore = 0 
i = 50

while i != 0:
	drop = random.randint(orel, reshka)
	if drop == orel:
		print('Орел')
		orelScore += 1
	else:
		print('Решка')
		reshkaScore += 1
	i -= 1
print('Орел ' + str(orelScore))
print('Решка ' + str(reshkaScore))
