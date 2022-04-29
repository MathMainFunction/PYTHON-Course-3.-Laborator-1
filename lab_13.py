value = int(input('Enter minutes: '))

minutes = value % (60*24) // 60
hour = value %  60
day = hour % 24

print('day:', day, 'hour:', hour, 'minutes:', minutes)

# if there is another method, i don't know about it
# i didn't see him in lectures, or he's not there

