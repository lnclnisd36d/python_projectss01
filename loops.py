# while loop
from datastructure import fruits

num=1
while num <=10:
    print(num)
    num+=1



# for loop
for num2 in range(1,11):
    print(num2)
fruits=["Banana","Oranges","Mangoes","Oranges"]

for i in fruits:
    print(i)

jina="eMobilis"

for n in jina:
    print(n)

number=[4,-5,6,-7,-8,7,1,9,0,-4]

sum_even=0

for m in number:
    if m % 2==0:
        sum_even+=m

print(f"the sum of even is {sum_even}")





