#create a program that checks if someone is eligible to vote by age
def voting_eligibility():
    try:
        age = int(input("Please enter your age: "))

        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")


voting_eligibility()

age=int(input("Enter yo age:"))

if age >=18:
    print("You are eligible to vote")
else:
    print("Naah you are young.")



