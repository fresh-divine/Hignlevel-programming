# debbuging

## indentation error

 File "c:\Users\ME\OneDrive\Desktop\highlevel-programming\0x15\Debbuging_lab.py", line 10, in <module>      
    index_error_bug()
    ~~~~~~~~~~~~~~~^^
  File "c:\Users\ME\OneDrive\Desktop\highlevel-programming\0x15\Debbuging_lab.py", line 6, in index_error_bug
    print(numbers[3])
          ~~~~~~~^^^
IndexError: list index out of range


The function tries to access index 3, but the list only has indexes 0, 1, and 2.
The reason is that index 3 does not exist
The assertion passed, demonstrating that the corrected function returns the expected value.

## key error

NameError: name 'type_error_bug' is not defined

### Symptom:

The function attempted to access a dictionary key that did not exist.

### Root cause:

The requested key was not present in the dictionary.

### Traceback:

Paste the actual traceback here.

### Fix:

Changed the lookup to an existing dictionary key.

## attribute_error_bug


### Symptom:

The function attempted to use an attribute or method that the object did not have.

### Root cause:

The string method name was incorrect.

### Traceback:

Paste the actual traceback here.

### Fix:

Changed the invalid method to the correct string method

### assertion
NameError: name 'attribute_error_bug' is not defined


## name_error_bug

### Symptom:

The function referred to a variable name that was not defined.

### Root cause:

The variable name was misspelled.

### Traceback:

Paste the actual traceback here.

### Fix:

Corrected the variable name.

### Assertion:

NameError: name 'name_error_bug' is not defined

## attribute_error_bug

### Symptom:

The function attempted to use an attribute or method that the object did not have.

### Root cause:

The string method name was incorrect.

### Traceback:

Paste the actual traceback here.

### Fix:

Changed the invalid method to the correct string method.

### Assertion:


## name_error_bug

### Symptom:

The function referred to a variable name that was not defined.

### Root cause:

The variable name was misspelled.

### Traceback:

Paste the actual traceback here.

### Fix:

Corrected the variable name.

### Assertion: