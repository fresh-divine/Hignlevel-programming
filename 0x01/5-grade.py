#!/usr/bin/python

score =int(input("Enter the students score:"))

if score >=90 and score <=100:
    print("Your grade is A")
elif score >=80 and score <=89:
    print("Your grade is B")
elif score >=70 and score <=79:
    print("Your grade is C")
elif score >=60 and score <=69:
    print("Your grade is D")
elif score >=0 and score <=60:
    print("Grade F")
else:
    print("invalid score")