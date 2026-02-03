'''
#1
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.percentage = 0
        self.grade = ""

    def calculate_percentage_and_grade(self):
        self.percentage = (self.marks / 500) * 100

        if self.percentage >= 90:
            self.grade = "A"
        elif self.percentage >= 75:
            self.grade = "B"
        elif self.percentage >= 60:
            self.grade = "C"
        else:
            self.grade = "D"

    def display(self):
        print("\n--- Student Details ---")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", round(self.percentage, 2))
        print("Grade:", self.grade)


# -------- Runtime Input --------
student_id = int(input("Enter Student ID: "))
name = input("Enter Student Name: ")
marks = float(input("Enter Total Marks (out of 500): "))

s = Student(student_id, name, marks)
s.calculate_percentage_and_grade()
s.display()

#3
class ObjectCount:
    count = 0  

    def __init__(self):
        ObjectCount.count += 1
        print("Object created.")
        print("Total objects created:", ObjectCount.count)


obj1 = ObjectCount()
obj2 = ObjectCount()

#4
class student1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = student1("Mithi", 21)
print("Class name:", s1.__class__.__name__)
print("Object ID:", id(s1))
print("Instance variables:",s1.__dict__)


#5
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class student(person):
    def __init__(self, name, age, student_id, marks):
        super().__init__(name, age)
        self.student_id = student_id
        self.marks = marks

    def display_student(self):
        super().display_person()
        print("Student ID:", self.student_id)
        print("Marks:", self.marks)

s1 = student("ramesh", 30, 12345, 85)
s1.display_student()


#6

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("\nPerson Details")
        print("Name:", self.name)
        print("Age:", self.age)


class Teacher:
    def __init__(self, employee_id, subject):
        self.employee_id = employee_id
        self.subject = subject

    def display_teacher(self):
        print("\nTeacher Details")
        print("Employee ID:", self.employee_id)
        print("Subject:", self.subject)


class TeachPerson(Person, Teacher):
    #Derived class that inherits from both Person and Teacher
    def __init__(self, name, age, employee_id, subject):
        Person.__init__(self, name, age)
        Teacher.__init__(self, employee_id, subject)

    def display(self):
        # display both person and teacher details
        self.display_person()
        self.display_teacher()


def teach_demo():
    tp = TeachPerson("Dr. Priya", 40, 501, "Mathematics")
    tp.display()

import random

def random_numbers_demo():
    """Generate random integers within a user-specified range."""
    print("\nRandom Numbers Generator")
    while True:
        try:
            low = int(input("Enter lower bound (integer): "))
            high = int(input("Enter upper bound (integer): "))
            if high < low:
                print("Upper bound must be >= lower bound.")
                continue
            count = int(input("How many random numbers to generate? "))
            if count <= 0:
                print("Please enter a positive number for count.")
                continue
            break
        except ValueError:
            print("Please enter valid integers")

    unique = input("Unique numbers only? (y/N): ").strip().lower() == 'y'
    if unique and (high - low + 1) < count:
        print("Range too small for unique numbers, generating with duplicates instead.")
        unique = False

    if unique:
        numbers = random.sample(range(low, high + 1), count)
    else:
        numbers = [random.randint(low, high) for _ in range(count)]

    print("Generated numbers:", numbers)
    


if __name__ == "__main__":
    while True:
        print("\nSelect demo to run:")
        print("1. Teacher demo")
        print("2. Random numbers generator")
        print("0. Exit")
        choice = input("Choose (0/1/2): ").strip()
        if choice == '1':
            teach_demo()
        elif choice == '2':
            random_numbers_demo()
        elif choice == '0':
            break
        else:
            print("Invalid choice, try again.")


#8
import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius * radius
circumference = 2 * math.pi * radius

print("Area of the circle:", area)
print("Circumference of the circle:", circumference)

#9
phno=input("enter the phone number:")
if len(phno)==12 and phno[3]=='-' and phno[7]=='-':
    print("valid phone number")
else:
    print("invalid phone number")
'''
#9
# validate phone number using regex format xxx-xxx-xxxx
import re
phone_number = input("Enter phone number: ") 
pattern = r'^\d{3}-\d{3}-\d{4}$'
if re.match(pattern, phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")

#11
class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited Amount:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print("Withdrawn Amount:", amount)

    def check_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount("Mithilesh", "ACC101", 1000)

account.check_balance()
account.deposit(500)
account.withdraw(300)
account.check_balance()
#12
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} has not borrowed '{book.title}'")

    def display_borrowed_books(self):
        print(f"\nBooks borrowed by {self.name}:")
        if not self.borrowed_books:
            print("No books borrowed")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")

b1 = Book(1, "Python Programming", "Guido van Rossum")
b2 = Book(2, "Data Structures", "Mark Allen Weiss")


m1 = Member(101, "Mithilesh")

m1.borrow_book(b1)
m1.borrow_book(b2)
m1.display_borrowed_books()

m1.return_book(b1)
m1.display_borrowed_books()
