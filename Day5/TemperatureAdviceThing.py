Temperature = float(input("What's the temperature? "))
Humidity = float(input("What's the humidity? "))

if Temperature >= 30 and Humidity >= 60:
    print("Don't go outside. Stay inside. It's not worth it!")
elif Temperature >= 30 and Humidity < 60:
    print("Bad weather for campfires")
elif Temperature <= 29 and Temperature > 5:
    print("Perfect weather to go outside")
else:
    print("It's pretty cold outside")