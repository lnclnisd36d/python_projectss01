# creates a programme that calculates your bmi

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are underweight")
elif 18.5 <=bmi< 24.9:
    print("You are healthy weight")
elif 25 <=bmi< 29.9:
    print("You are overweight")
elif 30.0 <=bmi< 39.9:
    print("You are obese")
else:
    print("You are severely obese")