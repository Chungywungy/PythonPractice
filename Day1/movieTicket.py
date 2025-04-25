age = int(input("How old are you?"))

if age < 12:
    print("It costs $8 for your ticket")
elif age <= 17:
    print("It costs $10 for your ticket")
else:
    print("It costs $12 for your ticket")