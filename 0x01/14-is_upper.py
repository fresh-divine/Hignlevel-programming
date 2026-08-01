#!/usr/bin/python
"""a module that converts lower case to capital letter"""
def is_upper(str):
    result=""
    for char in str:
        if ord(char) >=97 and ord(char)<=122:
            result+= chr(ord(char)-32)
        else:
            result+=char
    return result


if __name__=="__main__":
    string =input("Enter any sentence of your choice: ")
    print(is_upper(string))
