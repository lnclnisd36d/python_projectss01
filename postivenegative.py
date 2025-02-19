def postivenegativenumbers():
    try:
        number = int(input("Please enter an integer: "))

        if number > 0:
            print("The number is a positive integer.")
        elif number < 0:
            print("The number is a negative integer.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

postivenegativenumbers()




number = int(input("Please enter an integer: "))

if number > 0:
    print("The number is a positive integer.")
elif number < 0:
    print("The number is a negative integer.")
else:
    print("The number is zero.")