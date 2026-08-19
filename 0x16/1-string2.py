#/usr/bin/python
"""practical slicing examples"""
email = "ada@example.com"

at_index = email.index("@")
username = email[:at_index]
print(username) 

domain = email[at_index + 1:]
print(domain)   

filename = "report.pdf"
extension = filename[-3:]
print(extension)   # 

word = "racecar"
print(word[::-1])  



name = "Python"
new_name = "J" + name[1:]
print(new_name)   # Jython


word="python"
print(word[2])