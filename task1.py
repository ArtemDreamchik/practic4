password = str(input("Enter password: "))
password_scnd = str(input("Enter password again: "))

if password == password_scnd:
    print("Success")
else:
    print("Passwords isn't matching. Try again.")