# in here would be a program to test if a number is even
print("This program tests if a number is even")

num = int(input("Enter a number"))
even_test = num % 2
if even_test != 0:
	print(num, "is not an even number, it's odd")
else: 
	print(num, "is even, thanks")

