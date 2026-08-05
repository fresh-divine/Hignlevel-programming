

attempts = 0
MAX_ATTEMPTS = 3

while attempts < MAX_ATTEMPTS:
    password = input("Enter password: ")

    if password == "secret123":
        print("Access granted.")
        break

    attempts += 1
    remaining = MAX_ATTEMPTS - attempts
    print(f"Incorrect. {remaining} attempts remaining.")
else:
    print("Account locked.")