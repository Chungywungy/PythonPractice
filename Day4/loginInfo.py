username = input("Username: ")
password = input("Password: ")

if username == "Banana":
    if password == "Apple":
        print("Welcome to the jungle")
    else:
        print("Wrong password")
elif password == "Apple":
    if username == "Banana":
        print("Welcome to the jungle")
    else:
        print("wrong username")
else:
    print("wrong password and username")