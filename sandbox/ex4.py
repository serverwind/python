#расчет скорости по дистанции и времени
distance = input('distance in meters: ')
time = input('time in minutes: ')

d = int(distance)
t = int(time)
tSeconds = t * 60

s = d / tSeconds
speed = str(s)

print('your speed: ' + speed + 'm/sec')
