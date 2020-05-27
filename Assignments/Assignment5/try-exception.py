#Exception for ZeroDivision Error
print("Enter the values for a and b for division of a by b")
a = int(input())
b = int(input())
try:
	print(a/b)
except ZeroDivisionError:
	print("A number cannot be divided by zero")


print("Enter a numeric string")
a = input()
try:
	print(a/3)
except TypeError:
	print("A string cannot be divided by a integer. Convert the type of string to integer")

#If you don't know which type of exception to raise, then don't specify the exception name

print("Enter a file you want to read")
a = input()
try:
	f = open(a, "r")
	m = f.read()
	print("This is the content of your file")
	print(m)
except:
	print("This file is not present in the current directory")
finally:
	print("Finally executes like a common print statement.")


#We can also raise a exception in python using raise keyword

print("I am trying to raise my exception")
try:
	raise Myerror("I deliberately raised this exception")
except:
	print("Myerror is not a defined exception")
