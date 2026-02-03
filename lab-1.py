# 1st que
import datetime

now = datetime.datetime.now()
print(now)

#2nd que

first_name = input("enter your first name:")
last_name = input("enter your last name:")
print("full name is", first_name + " " + last_name)
print ("name after reversed is", last_name + " " + first_name)

#3RD QUE
num1 = int(input("enter first number:"))
answer = num1 + int(str(num1)*2) + int(str(num1)*3)
print("the answer for is :", answer)

#4th que
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
total = a + b + c
if a == b == c:
    total = total * 3
    print("the sum is:", total)
else:
    print("the sum is:", total)

#5th que
x = int(input("enter the value of x:"))
y = int(input("enter the value of y:"))
result = (x + y) * (x + y)
print("the result is:", result)

#6th que
amount = float(input("enter the amount:"))
rate = float(input("enter the rate of interest:"))
year = float(input("enter the time in years:"))
simple_interest = (amount * rate * year) / 100
print("the simple interest is:", simple_interest)

#7th que
s = input("enter the value:")
print(int(float(s)))
print(int(s))
print(float(s))

#8th que
num = int(input("enter the number:"))
total = (num*(num + 1)) / 2
print(f"the sum of {num} is:", total)

#9th que
original_n = input("enter the number:")
digit_sum = sum(int(d) for d in original_n if d.isdigit())
print(f"the sum of digits of {original_n} is:", digit_sum)

#10th que
ch = input("enter the character:")
print(ord(ch))

#11th que
s = input("enter the string:")
print(s.isnumeric())

#12th que
n = int(input("enter the number:"))
for i in range(n,0,-1):
    print("*" * i)

#13th que
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        print(i, end = ",")

#14th que
import math

C = 50
H = 30
values = input("enter D values separated by comma:")
D = values.split(",")
result = []
for d in D:
    Q = round(math.sqrt((2 * C * int(d)) / H))
    result.append(Q)
print(",".join(map(str, result)))

#15th que
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print(chr(ch), end="")
    print("")
    ch += 1

