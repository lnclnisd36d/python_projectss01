num=float(input("Enter your first number:"))
num1=float(input("Enter second number:"))
operator=input("Enter the operator.")

if operator == '+':
    result=num+num1
    print(f"the result of {num}{operator}{num1} is {result}")

elif operator == '-':
    result=num-num1
    print(f"the result of {num}{operator}{num1} is {result}")

elif operator == '*':
    result=num*num1
    print(f"the result of {num}{operator}{num1} is {result}")

elif operator == '/':
    if num1 !=0:
        result=num/num1
        print(f"The result of {num} {operator} {num1} is {result}")
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator")






