# this program checks if the number entered by the user is odd
print("You would have to enter a number to be checked")

# inputing a number
num = int(input("Please enter a number:"))
odd_test = num % 2
if odd_test != 0:
	print (num, "is an odd number")
else:
	print(num, "is an even number")
