#!/usr/bin/python
"""a module that converts lower case to capital letter"""
def is_lower(str):
    result=""
    for char in str:
        if ord(char) >=65 and ord(char)<=90:
            result+= chr(ord(char)+32)
        else:
            result+=char
    return result


if __name__=="__main__":
    string =input("Enter any sentence of your choice: ")
    print(is_lower(string))



    