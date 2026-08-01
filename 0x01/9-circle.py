#!/usr/bin/python

def circle(pi, r):
    return pi*r


if __name__=="__main__":
    pi=22/7
    r=int(input("Enter the raidus of the circle:"))
    result=circle(pi,r)
    print(f"your answer is {result}")
