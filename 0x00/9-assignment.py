#!/url/bin/sh
""" a module that handles assignment operations"""
num =int(input("enter any number of your choice: "))


num += 2 # short hand
#num = num + 2 # opposite
print("Addition assignment {}".format(num))

num *=2
print("multiplication assignment {}".format(num))

num -= 2
print("subtraction assignment {}".format(num))

num /= 2
print("Division assignment {}".format(num))

num %= 2
print("Modulus assignment {}".format(num))

num **= 2
print("Exponential assignment {}".format(num))
