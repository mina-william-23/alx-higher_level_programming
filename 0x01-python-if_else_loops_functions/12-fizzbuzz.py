#!/usr/bin/python3
def fizzbuzz():
    pr = ''
    for i in range(1, 101):
        if (i % 15 == 0):
            pr = 'FizzBuzz'
        elif (i % 5 == 0):
            pr = 'Buzz'
        elif (i % 3 == 0):
            pr = 'Fizz'
        else:
            pr = i
        print(pr, end=' ')
