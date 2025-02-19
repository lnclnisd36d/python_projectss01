def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range (1, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    # get user input
try:
    number = int(input("Enter Your Number :"))
    if is_prime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
except ValueError:
    print("Insert a valid integer")




