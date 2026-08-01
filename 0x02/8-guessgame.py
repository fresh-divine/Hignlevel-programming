#!/usr/bin/python

"""a program that runs guess game"""

import random

trial=3
while trial !=0:
    guess = random.randint(1, 20)
    num=int(input("enter the guess number(1-20) : "))
    if num == guess:
        print("congratulations you won")
        break
    else:
        print("Try again")
    trial -=1
    