import datetime

year = int(input("what year were you born in?"))

age = datetime.datetime.now().year - year

if age > 100:
    print("wow you're",age,"years old, what are you doing here you bag of bones?")
    print("you'll be",age + 1,"years old if you make it through this year!")
elif age < 0:
    print("wow you're from",year,"what's it like in the future?")
    print("you'll be born in",year - datetime.datetime.now().year,"years")
else:
    print("wow you're",age,"years old!")
    print("you'll be",age + 1,"years old next year!")