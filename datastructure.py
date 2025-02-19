# list data structure
fruits=["Mangoes","Watermelon","Pineapples","Apples","Peaches"]

print(fruits)
print(f"I love eating {fruits[2]}")

numbers=[3,8,9,6,7,2,4,1,5,0]
numbers.sort()
numbers.append("Grapes")
numbers.pop(0)
numbers.reverse()
print(numbers[1])
print(numbers)


# tuple data structure
# its ordered
# it has index
# it is immutable

cars=("Mercedes Benz","BMW","Audi","Volkswagen","Subaru")
numm=(2,3,4,5,6,7,9,1,0,8,-7)

print(cars)
print(f"Japan produces {cars[4]}")
print(numm)
print(sorted(numm))



# set data structure
# not ordered
# no index

country={"Kenya","Uganda","Tanzania","Rwanda","Somalia","Afghanistan"}
print(country)
country.pop()
print(country)

# dictionary data structure
# key value


student= {"Name":"Lincoln" , "Age": 69,"Gender": "Male", "Phone Number": 254742710798}
student["Name"]="Kiprop"
print(f"My name is {student['Name']} and I am {student['Age']} years old also my gender is {student['Gender']} and my phone number is {student['Phone Number']}" )











