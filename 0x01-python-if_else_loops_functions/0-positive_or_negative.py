#!/usr/bin/python3
import random
number = random.randint(-10, 10)
message = ''
if (number == 0):
    message = 'zero'
elif (number < 0):
    message = 'negative'
else:
    message = 'positive'
print(f'{number:d} is {message:s}')
